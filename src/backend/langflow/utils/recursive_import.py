import importlib
import pkgutil
import builtins



# def import_all_modules(package_name: str):
#     package = importlib.import_module(package_name)
#     modules = []
#     for importer, modname, is_pkg in pkgutil.walk_packages(package.__path__):
#         print(f'Found submodule {modname} ({"is a package" if is_pkg else "is a module"}).')
#         full_module_name = f"{package.__name__}.{modname}"
#         if not is_pkg:
#             try:
#                 module = importlib.import_module(modname)
#                 modules.append(module)
#             except Exception as e:
#                 print(f"Error importing {full_module_name}: {e}")
#             try:
#                 module = importlib.import_module(full_module_name)
#                 modules.append(module)
#             except Exception as e:
#                 print(f"Error importing {full_module_name}: {e}")
#     return modules
def import_all_modules(package_name: str, modules=None):
    if modules is None:
        modules = []

    package = importlib.import_module(package_name)
    for importer, modname, is_pkg in pkgutil.walk_packages(package.__path__):
        full_module_name = f"{package.__name__}.{modname}"
        if hasattr(builtins, modname):
            full_module_name = modname
        try:
            # If it's a package, recursively call import_all_modules to load all its submodules.
            if is_pkg:
                import_all_modules(full_module_name, modules)
            else:
                module = importlib.import_module(full_module_name)
                modules.append(module)
        except Exception as e:
            print(f"Error importing {full_module_name}: {e}")

    return modules

def find_class_object(modules, class_name):
    for module in modules:
        if hasattr(module, class_name):
            return getattr(module, class_name)
    return None


def find_class_object_in_module(module: str, class_name: str):
    all_modules = import_all_modules(module)
    class_obj = find_class_object(all_modules, class_name)
    if class_obj is not None:
        print(f"Found {class_name}!")
        return class_obj
    else:
        print(f"{class_name} not found.")
