# CVT 

Image transforms used in deep learning training.

## installation

```bash
git clone https://git.vistel.cn/jie.wang/cvt.git
cd cvt
python setup.py develop
```

## usage

cfg.json
```json
{
    "sequence":{
        "sample": {
            "bright": {"scale": 0.1},
            "contrast": {"scale": 0.1},
            "hue": {"scale": 0.1}
        },
        "shuffle": {
            "vflip": {},
            "hflip": {},
            "rotate": {"degrees": 30}
        }
    }
}
```


```python
import cvt
import matplotlib.pyplot as plt

tfms = cvt.from_file('cfg.json')
img = cv.imread('image.jpg')[:,:,[2,1,0]]
data = {'image':img}
data = tfms(data)

plt.imshow(data['image'])
plt.show()
```


## modules

- compose transforms
1. Sequence
2. Shuffle
3. Sample

- color transforms
1. RandomBright
2. RandomContrast
3. RandomSaturation
4. RandomHue
5. RandomGamma

- geometry transforms
1. RandomHorizontalFlip
2. RandomVerticalFlip
3. RandomRotation
4. Resize
5. RandomResizedCrop

- tensor
1. ToTensor
2. is_numpy
3. is_pil
4. is_tensor
5. to_numpy
6. to_pil
7. to_tensor