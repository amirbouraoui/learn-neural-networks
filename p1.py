# RESOURCE : https://youtu.be/Wo5dMEP_BbI?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3

"""

 ○    ○    ○  (Input Neuron)
  \   |   /
   \  |  /
    \ | /
      ○       (Output Neuron)

"""

# Outputs of 3 neurons from a previous layer
inputs = [1.2, 5.1, 2.1]

# every unique input will have an associate weight
weights = [3.1, 2.1, 8.7]

# for every unique neuron has an unique bias
bias = 3

# Calculate output by multiplying inputs with weights and add bias
output = inputs[0] * weights[0] + \
         inputs[1] * weights[1] + \
         inputs[2] * weights[2] + \
         bias

print(output)

"""

 Inputs        Weights        Output
( 1.2 ) ───► [ 3.1 ] ───┬
( 5.1 ) ───► [ 2.1 ] ───┼──► ( Σ + 3 ) ───► ( Output )
( 2.1 ) ───► [ 8.7 ] ───┴

"""
