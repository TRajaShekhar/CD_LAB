{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO7ush1pBX81PawHHcW4tXp",
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
        "<a href=\"https://colab.research.google.com/github/TRajaShekhar/CD_LAB/blob/main/ex9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vetaIUqe57aA"
      },
      "outputs": [],
      "source": [
        "\n",
        "gram = {\n",
        "\t\"S\":[\"CC\"],\n",
        "\t\"C\":[\"aC\",\"d\"]\n",
        "}\n",
        "start = \"S\"\n",
        "terms = [\"a\",\"d\",\"$\"]\n",
        "\n",
        "non_terms = []\n",
        "for i in gram:\n",
        "\tnon_terms.append(i)\n",
        "gram[\"S'\"]= [start]\n",
        "\n",
        "\n",
        "new_row = {}\n",
        "for i in terms+non_terms:\n",
        "\tnew_row[i]=\"\"\n",
        "\n",
        "\n",
        "non_terms += [\"S'\"]\n",
        "# each row in state table will be dictionary {nonterms ,term,$}\n",
        "stateTable = []\n",
        "# I = [(terminal, closure)]\n",
        "# I = [(\"S\",\"A.A\")]\n",
        "\n",
        "def Closure(term, I):\n",
        "\tif term in non_terms:\n",
        "\t\tfor i in gram[term]:\n",
        "\t\t\tI+=[(term,\".\"+i)]\n",
        "\tI = list(set(I))\n",
        "\tfor i in I:\n",
        "\t\t# print(\".\" != i[1][-1],i[1][i[1].index(\".\")+1])\n",
        "\t\tif \".\" != i[1][-1] and i[1][i[1].index(\".\")+1] in non_terms and i[1][i[1].index(\".\")+1] != term:\n",
        "\t\t\tI += Closure(i[1][i[1].index(\".\")+1], [])\n",
        "\treturn I\n",
        "\n",
        "Is = []\n",
        "Is+=set(Closure(\"S'\", []))\n",
        "\n",
        "\n",
        "countI = 0\n",
        "omegaList = [set(Is)]\n",
        "while countI<len(omegaList):\n",
        "\tnewrow = dict(new_row)\n",
        "\tvars_in_I = []\n",
        "\tIs = omegaList[countI]\n",
        "\tcountI+=1\n",
        "\tfor i in Is:\n",
        "\t\tif i[1][-1]!=\".\":\n",
        "\t\t\tindx = i[1].index(\".\")\n",
        "\t\t\tvars_in_I+=[i[1][indx+1]]\n",
        "\tvars_in_I = list(set(vars_in_I))\n",
        "\t# print(vars_in_I)\n",
        "\tfor i in vars_in_I:\n",
        "\t\tIn = []\n",
        "\t\tfor j in Is:\n",
        "\t\t\tif \".\"+i in j[1]:\n",
        "\t\t\t\trep = j[1].replace(\".\"+i,i+\".\")\n",
        "\t\t\t\tIn+=[(j[0],rep)]\n",
        "\t\tif (In[0][1][-1]!=\".\"):\n",
        "\t\t\ttemp = set(Closure(i,In))\n",
        "\t\t\tif temp not in omegaList:\n",
        "\t\t\t\tomegaList.append(temp)\n",
        "\t\t\tif i in non_terms:\n",
        "\t\t\t\tnewrow[i] = str(omegaList.index(temp))\n",
        "\t\t\telse:\n",
        "\t\t\t\tnewrow[i] = \"s\"+str(omegaList.index(temp))\n",
        "\t\t\tprint(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')\n",
        "\t\telse:\n",
        "\t\t\ttemp = set(In)\n",
        "\t\t\tif temp not in omegaList:\n",
        "\t\t\t\tomegaList.append(temp)\n",
        "\t\t\tif i in non_terms:\n",
        "\t\t\t\tnewrow[i] = str(omegaList.index(temp))\n",
        "\t\t\telse:\n",
        "\t\t\t\tnewrow[i] = \"s\"+str(omegaList.index(temp))\n",
        "\t\t\tprint(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')\n",
        "\n",
        "\tstateTable.append(newrow)\n",
        "print(\"\\n\\nList of I's\\n\")\n",
        "for i in omegaList:\n",
        "\tprint(f'I{omegaList.index(i)}: {i}')\n",
        "\n",
        "\n",
        "#populate replace elements in state Table\n",
        "I0 = []\n",
        "for i in list(omegaList[0]):\n",
        "\tI0 += [i[1].replace(\".\",\"\")]\n",
        "print(I0)\n",
        "\n",
        "for i in omegaList:\n",
        "\tfor j in i:\n",
        "\t\tif \".\" in j[1][-1]:\n",
        "\t\t\tif j[1][-2]==\"S\":\n",
        "\t\t\t\tstateTable[omegaList.index(i)][\"$\"] = \"Accept\"\n",
        "\t\t\t\tbreak\n",
        "\t\t\tfor k in terms:\n",
        "\t\t\t\tstateTable[omegaList.index(i)][k] = \"r\"+str(I0.index(j[1].replace(\".\",\"\")))\n",
        "print(\"\\nStateTable\")\n",
        "\n",
        "print(f'{\" \": <9}',end=\"\")\n",
        "for i in new_row:\n",
        "\tprint(f'|{i: <11}',end=\"\")\n",
        "\n",
        "print(f'\\n{\"-\":-<66}')\n",
        "for i in stateTable:\n",
        "\tprint(f'{\"I(\"+str(stateTable.index(i))+\")\": <9}',end=\"\")\n",
        "\tfor j in i:\n",
        "\t\tprint(f'|{i[j]: <10}',end=\" \")\n",
        "\tprint()"
      ]
    }
  ]
}