import itertools
import os.path
import threading


__all__ = [
	"sanitize",
	"unused_file"
]


lock = threading.Lock()


def sanitize(filename):
	return (
		filename
			.replace("/", "")
			.replace("\"", "")
	)


def unused_file(filename):
	with lock:
		if os.path.exists(filename):
			filename, ext = os.path.splitext(filename)

			template = filename + " ({})" + ext

			filename = next(
				template.format(i)
				for i in itertools.count()
				if not os.path.exists(
					template.format(i)
				)
			)

			open(filename, "a").close() # Touch the file, so subsequent calls to this function
			                            # won't result in the same file name.

	return filename
