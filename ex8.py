{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQYAinLymD8MTdcKSbJO60",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TRajaShekhar/CD_LAB/blob/main/ex8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aFbO1COn5E3F"
      },
      "outputs": [],
      "source": [
        "# example 1\n",
        "gram = {\n",
        "\t\"E\":[\"2E2\",\"3E3\",\"4\"]\n",
        "}\n",
        "starting_terminal = \"E\"\n",
        "inp = \"2324232$\"\n",
        "\"\"\"\n",
        "# example 2\n",
        "gram = {\n",
        "\t\"S\":[\"S+S\",\"S*S\",\"i\"]\n",
        "}\n",
        "starting_terminal = \"S\"\n",
        "inp = \"i+i*i\"\n",
        "\"\"\"\n",
        "stack = \"$\"\n",
        "print(f'{\"Stack\": <15}'+\"|\"+f'{\"Input Buffer\": <15}'+\"|\"+f'Parsing Action')\n",
        "print(f'{\"-\":-<50}')\n",
        "\n",
        "while True:\n",
        "\taction = True\n",
        "\ti = 0\n",
        "\twhile i<len(gram[starting_terminal]):\n",
        "\t\tif gram[starting_terminal][i] in stack:\n",
        "\t\t\tstack = stack.replace(gram[starting_terminal][i],starting_terminal)\n",
        "\t\t\tprint(f'{stack: <15}'+\"|\"+f'{inp: <15}'+\"|\"+f'Reduce S->{gram[starting_terminal][i]}')\n",
        "\t\t\ti=-1\n",
        "\t\t\taction = False\n",
        "\t\ti+=1\n",
        "\tif len(inp)>1:\n",
        "\t\tstack+=inp[0]\n",
        "\t\tinp=inp[1:]\n",
        "\t\tprint(f'{stack: <15}'+\"|\"+f'{inp: <15}'+\"|\"+f'Shift')\n",
        "\t\taction = False\n",
        "\n",
        "\tif inp == \"$\" and stack == (\"$\"+starting_terminal):\n",
        "\t\tprint(f'{stack: <15}'+\"|\"+f'{inp: <15}'+\"|\"+f'Accepted')\n",
        "\t\tbreak\n",
        "\n",
        "\tif action:\n",
        "\t\tprint(f'{stack: <15}'+\"|\"+f'{inp: <15}'+\"|\"+f'Rejected')\n",
        "\t\tbreak"
      ]
    }
  ]
}