from .silence import (
    GapAnalyser,
    OpeningSilenceAnalyser,
    TrailingSilenceAnalyser
)

from .volume import LoudnessAnalyser


analysers = [
    GapAnalyser,
    LoudnessAnalyser,
    OpeningSilenceAnalyser,
    TrailingSilenceAnalyser
]
