# Handwritten Character Recognition

This project is an implementation of a Convolutional Neural Network (CNN) for recognizing and classifying handwritten characters. The project includes various stages such as data preprocessing, model training, evaluation, and testing.

## Project Structure

```
handwritten-character-recognition/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── examples/
│
├── src/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_testing.ipynb
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── visualize.py
│
├── tests/
│   ├── test_data_loading.py
│   ├── test_preprocessing.py
│   └── test_model.py
│
├── results/
│   ├── training_logs/
│   └── model_checkpoints/
│
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OzcanCevik/handwritten-character-recognition.git
   cd handwritten-character-recognition
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Data Preprocessing

The data preprocessing stage involves the following steps:
1. **Grayscale Conversion:** Convert the input images to grayscale to reduce complexity.
2. **Normalization:** Scale the pixel values to a range of 0-1 to improve the model's convergence speed.
3. **Resizing:** Resize images to a consistent dimension (e.g., 32x32) for uniform input to the CNN.

You can find the data preprocessing notebook in `src/data_preprocessing.ipynb`.

## Model Training

The model is a Convolutional Neural Network (CNN) designed for character recognition. The training process includes:
- **Convolutional Layers:** Extracting features from the input images.
- **Pooling Layers:** Reducing dimensionality while retaining important features.
- **Fully Connected Layers:** Making predictions based on the extracted features.

Training details can be found in `src/model_training.ipynb`.

## Model Testing

Once the model is trained, it can be tested using the test dataset. The evaluation metrics will help assess the performance of the model.

Testing code is available in `src/model_testing.ipynb`.

## Results

The results of the model training, including accuracy, loss, and confusion matrix, are stored in the `results/` directory. Model checkpoints and training logs are also saved for further analysis.

## Usage

To run the project, you can simply execute the `main.py` script:

```bash
python main.py
```

This script will load the data, preprocess it, train the model, and evaluate it.

## Tests

Unit tests are provided in the `tests/` directory to ensure the reliability of each component in the pipeline.

To run the tests, use:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## Acknowledgments

Special thanks to all contributors and the open-source community for their support.

[View the live site](https://ozcancevik.github.io/handwritten-character-recognition/)

```

