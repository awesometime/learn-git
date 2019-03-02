```python
#替代os.path.join()函数

from pathlib import Path

dataset = 'wiki_images'
datasets_root = Path('/path/to/datasets/') 

train_path = datasets_root / dataset / 'train'
test_path = datasets_root / dataset / 'test'

for image_path in train_path.iterdir():
    with image_path.open() as f: # note, open is a method of Path object
        # do something with an image


p.exists()
p.is_dir()
p.parts()
p.with_name('sibling.png') # only change the name, but keep the folder
p.with_suffix('.jpg') # only change the extension, but keep the folder and the name
p.chmod(mode)
p.rmdir()
```
