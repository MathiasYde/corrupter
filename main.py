import base64
import os
import click
import random
import uuid

@click.command()
@click.option("--file_path", "--file", required=True)
@click.option("--bulk_size", "--bulk", default=32)
@click.option("--cuts", default=4)
@click.option("--export_directory", "--export", required=True)
def main(file_path, bulk_size: int, cuts: int, export_directory):
	with open(file_path, "rb") as file:
		image = base64.b64encode(file.read()).decode("ascii")

	for _ in range(bulk_size):
		corrupt = image
		for _ in range(cuts):
			i = random.randint(0, len(corrupt))
			corrupt = corrupt[:i] + corrupt[i+1:]

		filename = f"{uuid.uuid1()}.png"
		with open(os.path.join(export_directory, filename),"wb") as file:
			file.write(base64.b64decode(corrupt))

if __name__ == "__main__":
	main()