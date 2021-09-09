import tensorflow as tf

def get_model() :
    max_length = 15
    max_words = 20000

    model = tf.keras.Sequential([
                             tf.keras.layers.Embedding(max_words, 64, input_length=max_length),
                             tf.keras.layers.GlobalAveragePooling1D(),
                             tf.keras.layers.Dense(64, activation='relu'),
                             tf.keras.layers.Dense(64, activation='relu'),
                             tf.keras.layers.Dense(16, activation='relu'),
                             tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.load_weights('./model1/checkpoint')

    return model