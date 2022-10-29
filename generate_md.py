import os


class Blog_Generate_md():
	def __init__(self, path):
		self.path = path
		self.postfix_list = set([
			'exe', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf',
			'jpg', 'png', 'bmp', 'jpeg', 'gif',
			'zip', 'rar', 'tar', 'bz2', '7z', 'gz',
			'flv', 'mp4', 'avi', 'wmv', 'mkv',
			'apk',
		])

	def filter(self, path):
		"""filter 过滤不需要的文件，过滤后缀"""
		postfix = path.split('.')[-1].lower()
		if postfix in self.postfix_list:
			return "Null"

	def path_generate(self):
		path_list = os.walk(self.path)
		# path_list = os.listdir("./data")
		# print(path_list)
		# print(list(path_list))
		for dirpath, dirnames, filenames in path_list:
			# for
			# path = os.path.join(dirpath, dirnames, filenames)
			print(dirpath, dirnames, filenames, sep="\t\t")

	def main(self):
		path_list = self.path_generate()


if __name__ == '__main__':
	path = "./data"
	Blog_Generate_md(path).main()
