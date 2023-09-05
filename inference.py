from models.tunet import TUNet
model = TUNet(None,None)
for name, param in model.named_parameters():
        print(f"Parameter name: {name}")