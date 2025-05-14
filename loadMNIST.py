from zipfile import ZipFile
def load_mnist():
  train_csv_path = Path("datasets/mnist_train.csv")
  test_csv_path = Path("datasets/mnist_test.csv")
  train_zip_path = Path("datasets/mnist_train.csv.zip")
  test_zip_path = Path("datasets/mnist_test.csv.zip")
  if not train_csv_path.is_file():
    Path("datasets").mkdir(parents=True, exist_ok=True)
    #url_train = "https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_train_100.csv"
    url_train = "https://github.com/nederjair/mnist_dataset/raw/refs/heads/main/mnist_train.zip"
    urllib.request.urlretrieve(url_train, train_zip_path)

  if not test_csv_path.is_file():
    Path("datasets").mkdir(parents=True, exist_ok=True)
    #url_test = "https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_test_10.csv"
    url_test = "https://github.com/nederjair/mnist_dataset/raw/refs/heads/main/mnist_test.zip"
    urllib.request.urlretrieve(url_test, test_zip_path)

  # loading the temp.zip and creating a zip object
  with ZipFile("datasets/mnist_test.csv.zip", 'r') as zObject:
      zObject.extractall(path="datasets/")
  with ZipFile("datasets/mnist_train.csv.zip", 'r') as zObject:
    zObject.extractall(path="datasets/")

  file = open('datasets/mnist_train.csv', 'r')
  train_data_list = file.readlines()
  file.close()
  file = open('datasets/mnist_test.csv', 'r')
  test_data_list = file.readlines()
  file.close()
  return train_data_list, test_data_list
