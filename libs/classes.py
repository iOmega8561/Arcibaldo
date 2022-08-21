class formats:
	header = "\033[95m"
	blue = "\033[94m"
	cyan = "\033[96m"
	green = "\033[92m"
	warn = "\033[93m"
	fail = "\033[91m"
	endc = "\033[0m"
	bold = "\033[1m"
	uline = "\033[4m"
	warnStr = f"{warn}Warning:{endc}"
	errStr = f"{fail}Error:{endc}"
	msgStr = f"{bold}Message:{endc}"
	succStr = f"{green}Message:{endc}"
	selStr = f"{bold}{{}}){endc} {{}} {bold}({{}}){endc}\n"

class profile:
        def __init__(self, name, type, pkgs, units, groups):
                self.name = name
                self.type = type
                self.pkgs = pkgs
                self.units = units
                self.groups = groups

class file:
	def __init__(self, name, path, text):
		self.name = name
		self.path = path
		self.text = text
