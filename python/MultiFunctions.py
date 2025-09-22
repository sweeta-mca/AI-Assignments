class HopeFunctions:
    @staticmethod
    def aiSubFields():
        ai_fields = ["Machine Learning", "Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in ai_fields:
            print(field)
    def isOdd(self,num):
        return (num % 2 !=0)    
    def oddEven(self,num):
        if self.isOdd(num) :
            print(f"{num} is Odd Number")
        else:
            print(f"{num} is Even Number")
    def eligibleForMarriage(self,gender,age):
        eligible = False
        if(gender == "male" and age > 21):
            eligible= True
        if(gender == "female" and age >18):
            eligible = True
        return eligible
    def percentage(self,s1,s2,s3,s4,s5):
        total = s1+s2+s3+s4+s5
        percentage = (total/500)*100
        print(f"Total : {total}")
        print(f"Percentage : {percentage}")
    @staticmethod
    def area(height,breadth):
        return 0.5*breadth*height
    @staticmethod
    def perimeter(height1,height2,breadth):
        return height1+height2+breadth
    @staticmethod
    def triangle():
        print("Find Area of Triangle")
        height = float(input("Height:"))
        breadth = float(input("Breadth:"))
        print("Area Formula : (Height*Breadth)/2")
        a = HopeFunctions.area(height,breadth)
        print(f"Area of Triangle:{a}")
        print("Find Perimeter of Triangle")
        height1 = float(input("Height:"))
        height2= float(input("Height2:"))
        breadth = float(input("Breadth:"))
        p = HopeFunctions.perimeter(height1,height2,breadth)
        print("Perimeter Formula : Height1+Height2+Breadth")
        print(f"Perimeter of Triangle:{p}") 
