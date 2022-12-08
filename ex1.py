{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP42ami2DdoemMWL6Q1VKIa",
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
        "<a href=\"https://colab.research.google.com/github/TRajaShekhar/CD_LAB/blob/main/ex1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "PHQzxGRfrH0R",
        "outputId": "4df33256-5bce-4ab8-cf7b-4f29b8b87975"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-0bba9413a254>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     66\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0marr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     67\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 68\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'e1-example.txt'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     69\u001b[0m         \u001b[0mtext\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     70\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'e1-example.txt'"
          ]
        }
      ],
      "source": [
        "keywords = {\"auto\",\"break\",\"case\",\"char\",\"const\",\"continue\",\"default\",\"do\",\n",
        "\"double\",\"else\",\"enum\",\"extern\",\"float\",\"for\",\"goto\",\n",
        "\"if\",\"int\",\"long\",\"register\",\"return\",\"short\",\"signed\",\n",
        "\"sizeof\",\"static\",\"struct\",\"switch\",\"typedef\",\"union\",\n",
        "\"unsigned\",\"void\",\"volatile\",\"while\",\"printf\",\"scanf\",\"%d\",\"include\",\"stdio.h\",\"main\"}\n",
        "\n",
        "operators = {\"+\",\"-\",\"*\",\"/\",\"<\",\">\",\"=\",\"<=\",\">=\",\"==\",\"!=\",\"++\",\"--\",\"%\"}\n",
        "\n",
        "delimiters = {'(',')','{','}','[',']','\"',\"'\",';','#',',',''}\n",
        "\n",
        "def detect_keywords(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in keywords:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_operators(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in operators:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_delimiters(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in delimiters:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_num(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\ttry:\n",
        "\t\t\ta = int(word)\n",
        "\t\t\tarr.append(word)\n",
        "\t\texcept:\n",
        "\t\t\tpass\n",
        "\treturn list(set(arr))\n",
        "\"\"\"\n",
        "this is original function for detecting identifier\n",
        "def is_identifier(token):\n",
        "    if token[0] in numbers or token in keywords:\n",
        "        return False\n",
        "    else:\n",
        "        return identifier(token)\n",
        "def identifier(token):\n",
        "    if len(token)<2 and (token[0] in alphabets or token[0] in numbers or token[0] == \"_\"):\n",
        "        return True\n",
        "    elif token[0] in alphabets or token[0] in numbers or token[0] == \"_\":\n",
        "        return identifier(token[1:])\n",
        "    else:\n",
        "        return False\n",
        "\"\"\"\n",
        "def detect_identifiers(text):\n",
        "\tk = detect_keywords(text)\n",
        "\to = detect_operators(text)\n",
        "\td = detect_delimiters(text)\n",
        "\tn = detect_num(text)\n",
        "\tnot_ident = k + o + d + n\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word not in not_ident:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn arr\n",
        "\n",
        "with open('e1-example.txt') as t:\n",
        "\ttext = t.read().split()\n",
        "\n",
        "print(\"Keywords: \",detect_keywords(text))\n",
        "print(\"Operators: \",detect_operators(text))\n",
        "print(\"Delimiters: \",detect_delimiters(text))\n",
        "print(\"Identifiers: \",detect_identifiers(text))\n",
        "print(\"Numbers: \",detect_num(text))"
      ]
    }
  ]
}