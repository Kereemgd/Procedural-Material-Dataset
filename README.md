# Procedural Material Dataset
Optimized Procedural Material Dataset for Blender And review of an AI based approach for generating them.

<div align="center">
    <img src="https://github.com/user-attachments/assets/974a8843-6629-4408-8bd7-c2111fd4576f" alt="Chicken" width="300"/>
</div>

# What's Blender ?
Blender is a powerful 3D software that is open-source and free to use. It is used for a wide range of tasks in 3D graphics

# Blender Material Nodes
Blender's Material Nodes are incredible, they allow users to create and edit materials, textures, and effects using a node-based system. In this system, various nodes are connected together to define how a material or surface behaves with respect to light, reflection, color, transparency, and other physical properties.
![editors_texture-node_introduction_types-combined](https://github.com/user-attachments/assets/792b2519-c40b-402c-8bc6-dd1a65eeef6c)


# Overview
As you may gather from the description, this repository contains a highly optimized version of a dataset featuring text-based representations of procedural material nodes in Blender. Thanks to [Brendan Parmer](https://github.com/BrendanParmer), the developer of the Node-To-Python addon, I successfully converted all of the materials into text. With a great deal of patience over the past five months, I was able to optimize them further. There are more than 2.000 materials in the folder.

![ezgif-3-134510a15e](https://github.com/user-attachments/assets/182f7032-9e25-4e1f-896f-31dc50f10bfd)

I attempted to train language models to generate procedural materials, and while the results were promising, with excellent outputs occurring at a rate of 1 in 50, I ultimately decided against further development and deployment due to the required effort. Therefore, I am releasing the dataset I used, along with some insights gained from this five-month journey. Please, if you use the dataset, let me know.

# Dataset
Raw, optimized, and string-indexed versions of the dataset can be found in the link below:

https://drive.google.com/drive/folders/1I3dyU3Kv7P9blAAAqPvPLdqst_otkoNB?usp=sharing

<h3 align="center">Distribution of the File Sizes:</h3>
<div align="center">
    <img src="https://github.com/user-attachments/assets/a8508093-7882-4fb0-8a7d-dd90ef1bd867" alt="AllMaterialFileSizeDistribution" width="800"/>
</div>

<h3 align="center">Effect of Optimization:</h3>
<div align="center">
    <img src="https://github.com/user-attachments/assets/60ed86bd-6f84-4b5f-bb73-1b179800f062" alt="Effect of Optimization" width="800"/>
</div>

# Preprocessing Stage
1- Erasing the Location, Dimension and unnecessary comments.
![image](https://github.com/user-attachments/assets/62d90389-0d3b-41aa-bb8a-532cd6a544e4)

2- Decreasing Float Precision.

![floatoptız](https://github.com/user-attachments/assets/7f96c49f-e647-4265-a988-d818435491a3)

3- Erasing default node values.

So, if you use NodeToPython addon you'll see that it exports every value of every node, including the default ones. So, ı erased the default ones, that caused %40 loss in token count. There's a file "Useful Codes/dataset_optimizer.py" - ı know the code is unnecessarily complicated - but you can use it to optimize raw dataset for blender 4.1

![principled_bsdf](https://github.com/user-attachments/assets/9b961ebf-37d5-4960-9503-8b6ad454875c)

# Displaying Text Files

First, select the text file you want to display and copy the text init:

![select_copy_opt](https://github.com/user-attachments/assets/5d94a829-02d3-43a3-8ce7-5dfaee6a62d3)


Then, head over the Blender "Scripting" layout and paste the text:

![paste_exec_1](https://github.com/user-attachments/assets/45010dbe-321e-4a87-863e-55520e8f162f)


After that, execute the code and head over the "Shading" layout:

![execute](https://github.com/user-attachments/assets/e8d6663a-9ed4-469c-bfa5-d5b17dccbbd9)


Select the material:

![select_mat_opt](https://github.com/user-attachments/assets/16db4a96-42f3-4333-8e2c-1eb481a0cf73)


Enjoy :)

![enjoy2](https://github.com/user-attachments/assets/1c53b9c0-ff07-44e9-be89-8a2cb2900779)

## Model Training Process
I preferred to use LLMs to process my data due to their efficiency in handling '.txt' files and robust debugging capabilities. To avoid training a large-scale transformer model from scratch, I leveraged pretrained weights. Specifically, I fine-tuned OpenAI's GPT-4o mini base model, which offers fast inference and relatively low costs.

The dataset I used consists of 995 materials, each under 10KB in size, with a maximum token length of 3,500

![train_diagram](https://github.com/user-attachments/assets/66444097-3c67-48ca-b2e9-adcf43f04727)

-Hyperparameters

- Batch Size : 2
- Epochs : 4
- Lr Multiplier : 1-e4

![c0b696c7-3741-43ff-baf6-64b30f5f25ea](https://github.com/user-attachments/assets/1be27a4b-0838-4c87-adb4-fb7f6b09c09d)

- Using optimized dataset prevented model to generate outputs with syntax errors, and allowing it for more accurate outputs
- str_text_files - Kopya folder contains txt files of dictionaries of number indexes and string indexes
- String Indexed dataset didn't make as much succes as ı expected
- You can use "JSON.py" to convert a folder to json extension dataset
# Some Materials Generated By fine-tuned Gpt4-o mini

| <img src="https://github.com/user-attachments/assets/c282b5b2-25ba-4296-ba69-d371e87ac604" alt="Cracked Ice" width="150"/> | <img src="https://github.com/user-attachments/assets/80d45852-9852-46ba-ad5b-803668deec6d" alt="Dot" width="150"/> | <img src="https://github.com/user-attachments/assets/6c7cb1ec-b850-4300-a424-337969e9ca24" alt="Galaxy with Stars" width="150"/> | <img src="https://github.com/user-attachments/assets/3628358f-4616-427d-a9a3-0dc79f11e6be" alt="Gold" width="150"/> |
|:----------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| **Cracked Ice** | **Dot** | **Galaxy with Stars** | **Gold** |
| <img src="https://github.com/user-attachments/assets/9f991df6-8009-407a-888e-ff9cf4211047" alt="Rough Wood" width="150"/> | <img src="https://github.com/user-attachments/assets/bade204c-f409-4128-9e8a-8566fe9056d3" alt="Procedural Blood" width="150"/> | <img src="https://github.com/user-attachments/assets/0fef09c4-b4f1-4f9f-842c-da3cbbef76fa" alt="Stone" width="150"/> | <img src="https://github.com/user-attachments/assets/4d44498c-a493-4fc7-8fa0-89d7092d07e6" alt="Abstract" width="150"/> |
| **Rough Wood** | **Procedural Blood** | **Stone** | **Abstract** |

# Future Work
- to be written
