this repository is used for trying to packaging module sensehi.
reference to:
https://zhuanlan.zhihu.com/p/73199573
Key commnad： 
python3 -m pip install --user --upgrade setuptools wheel  
python3 setup.py sdist bdist_wheel 打包 
python3 -m pip install --user --upgrade twine 
twine upload dist/*