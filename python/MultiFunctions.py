{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a6c7abb2-b40e-4ad1-9726-0d73413d7fd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class HopeFunctions:\n",
    "    @staticmethod\n",
    "    def aiSubFields():\n",
    "        ai_fields = [\"Machine Learning\", \"Neural Networks\",\"Vision\",\"Robotics\",\"Speech Processing\",\"Natural Language Processing\"]\n",
    "        print(\"Sub-fields in AI are:\")\n",
    "        for field in ai_fields:\n",
    "            print(field)\n",
    "    def isOdd(self,num):\n",
    "        return (num % 2 !=0)    \n",
    "    def oddEven(self,num):\n",
    "        if self.isOdd(num) :\n",
    "            print(f\"{num} is Odd Number\")\n",
    "        else:\n",
    "            print(f\"{num} is Even Number\")\n",
    "    def eligibleForMarriage(self,gender,age):\n",
    "        eligible = False\n",
    "        if(gender == \"male\" and age > 21):\n",
    "            eligible= True\n",
    "        if(gender == \"female\" and age >18):\n",
    "            eligible = True\n",
    "        return eligible\n",
    "    def percentage(self,s1,s2,s3,s4,s5):\n",
    "        total = s1+s2+s3+s4+s5\n",
    "        percentage = (total/500)*100\n",
    "        print(f\"Total : {total}\")\n",
    "        print(f\"Percentage : {percentage}\")\n",
    "    @staticmethod\n",
    "    def area(height,breadth):\n",
    "        return 0.5*breadth*height\n",
    "    @staticmethod\n",
    "    def perimeter(height1,height2,breadth):\n",
    "        return height1+height2+breadth\n",
    "    @staticmethod\n",
    "    def triangle():\n",
    "        print(\"Find Area of Triangle\")\n",
    "        height = float(input(\"Height:\"))\n",
    "        breadth = float(input(\"Breadth:\"))\n",
    "        print(\"Area Formula : (Height*Breadth)/2\")\n",
    "        a = HopeFunctions.area(height,breadth)\n",
    "        print(f\"Area of Triangle:{a}\")\n",
    "        print(\"Find Perimeter of Triangle\")\n",
    "        height1 = float(input(\"Height:\"))\n",
    "        height2= float(input(\"Height2:\"))\n",
    "        breadth = float(input(\"Breadth:\"))\n",
    "        p = HopeFunctions.perimeter(height1,height2,breadth)\n",
    "        print(\"Perimeter Formula : Height1+Height2+Breadth\")\n",
    "        print(f\"Perimeter of Triangle:{p}\") \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
