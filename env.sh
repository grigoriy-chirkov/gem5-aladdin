module load gcc-toolset/10
module load anaconda3/2022.5

conda activate aladdin
export LLVM_HOME=/tigress/gchirkov/llvm-project/build
export LLVM_ROOT=/tigress/gchirkov/llvm-project/build
export PATH=$LLVM_HOME/bin:$PATH
export ALADDIN_HOME=/tigress/gchirkov/gem5-aladdin/src/aladdin
export TRACER_HOME=/tigress/gchirkov/LLVM-Tracer/install/usr/local