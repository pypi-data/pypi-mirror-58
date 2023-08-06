# coding: utf-8
from .chunks.chunkframeworkbase import ChunkFrameworkBase
from .chunks.chunkframework import ChunkFramework
from .chunks.chunks import Chunks, TokChunks

from .modifytokens.adjusttokens import AdjustTokens
from .modifytokens.cqlmatcher import CQLMatcher
from .modifytokens.mergedagdra import MergeDagdra
from .modifytokens.mergingmatcher import MergingMatcher
from .modifytokens.replacingmatcher import ReplacingMatcher
from .modifytokens.splitaffixed import split_affixed
from .modifytokens.splittingmatcher import SplittingMatcher
from .modifytokens.tokenmerge import TokenMerge
from .modifytokens.tokensplit import TokenSplit

from .text.pipelinebase import PipelineBase
from .text.text import Text

from .textunits.bostring import BoString
from .textunits.bosyl import BoSyl
from .textunits.sylcomponents import SylComponents

from .third_party.cqlparser import Query, parse_cql_query, replace_token_attributes

from .tokenizers.token import Token
from .tokenizers.tokenize import Tokenize
from .tokenizers.wordtokenizer import WordTokenizer
from .tokenizers.sentencetokenizer import sentence_tokenizer
from .tokenizers.paragraphtokenizer import paragraph_tokenizer
from .tokenizers.chunktokenizer import ChunkTokenizer

from .tries.basictrie import BasicTrie
from .tries.trie import Trie

from .utils.expose_data import expose_data
from .utils.get_data import get_data

from .config import Config
from .vars import *
from .vars import __version__

from pathlib import Path


def cwd():
    return Path(__file__).parent.resolve()


# download trie data from botok-data
get_data(
    "https://github.com/Esukhia/botok-data/archive/master.zip",
    Path(__file__).parent / "resources",
)
