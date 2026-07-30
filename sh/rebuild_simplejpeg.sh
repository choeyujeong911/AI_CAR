sudo apt install -y cmake nasm build-essential python3-dev libjpeg-dev
python -m pip install --upgrade pip setuptools wheel cython
python -m pip install --no-cache-dir --no-deps --no-binary=simplejpeg --no-build-isolation --force-reinstall simplejpeg
