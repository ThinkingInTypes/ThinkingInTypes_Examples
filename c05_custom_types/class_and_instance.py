# class_and_instance.py

def show_dicts(obj: object, obj_name: str, info: str = ""):
    cls = obj.__class__
    cls_name = cls.__name__

    cls_dict = {k: v for k, v in cls.__dict__.items() if not k.startswith("__")}
    obj_dict = obj.__dict__

    print(f" {info} ".center(30, "-"))
    print(f"{cls_name}.__dict__ (class attributes):")
    for attr in cls_dict.keys():
        value = cls_dict[attr]
        note = ""
        if attr in obj_dict and obj_dict[attr] != value:
            note = "  # overridden by instance"
        print(f"  {attr}: {value}{note}")

    print(f"\n{obj_name}.__dict__ (instance attributes):")
    for attr in cls_dict.keys():
        if attr in obj_dict:
            print(f"  {attr}: {obj_dict[attr]}")
        else:
            print(f"  {attr}: <not present>")

    print("\ndirect access:")
    for attr in cls_dict.keys():
        print(f"{obj_name}.{attr} is {getattr(obj, attr)}")
