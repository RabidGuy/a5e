

if __name__ == '__main__':
	import os

	directory_contents = os.listdir()
	module_filenames = [f for f in directory_contents if f.startswith("analyze_") and f.endswith(".py")]
	modules = [__import__(m[:-3]) for m in module_filenames]
	# print(modules)

	# XXX Find Analyzer subclasses in modules and run each.
