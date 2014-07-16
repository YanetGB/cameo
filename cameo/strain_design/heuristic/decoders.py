# Copyright 2014 Novo Nordisk Foundation Center for Biosustainability, DTU.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from cobra.manipulation.delete import find_gene_knockout_reactions


class KnockoutDecoder(object):
    def __init__(self, representation, model, *args, **kwargs):
        super(KnockoutDecoder, self).__init__(*args, **kwargs)
        self.representation = representation
        self.model = model

    def __call__(self, individual):
        raise NotImplementedError


class ReactionKnockoutDecoder(KnockoutDecoder):
    def __init__(self, *args, **kwargs):
        super(ReactionKnockoutDecoder, self).__init__(*args, **kwargs)

    def __call__(self, individual):
        reactions = [self.model.reactions.get_by_id(self.representation[index]) for index in individual]
        return [reactions, reactions]


class GeneKnockoutDecoder(KnockoutDecoder):
    def __init__(self, *args, **kwargs):
        super(GeneKnockoutDecoder, self).__init__(*args, **kwargs)

    def __call__(self, individual):
        genes = [self.model.genes.get_by_id(self.representation[index]) for index in individual]
        reactions = find_gene_knockout_reactions(self.model, genes)
        return [reactions, genes]