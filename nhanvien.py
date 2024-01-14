import math
from People import People
from unidecode import unidecode
from datetime import datetime

class nhanvien:
    nhan_vien=[]
    def sortbyID(self):
        self.nhan_vien.sort(key=lambda x:x.EmCode,reverse=False)
    def sortbyName(self):
        self.nhan_vien.sort(key=lambda x:x.Name,reverse=False)
    def sortbyDate(self):
        self.nhan_vien.sort(key=lambda x:x.Date,reverse=False)
    def sortbySalary(self):
        self.nhan_vien.sort(key=lambda x:x.Salary,reverse=False)
    def sortbyPosition(self):
        self.nhan_vien.sort(key=lambda x:x.Position,reverse=False)
    def LenNv(self):
        return self.nhan_vien.__len__()
    def insertion_sort(self,field):
        n=self.LenNv()
        Nv=self.nhan_vien
        for i in range(n):
            current_nv=Nv[i]
            j=i-1
            while j>=0:
                if field == 'Name' or field == 'Salary' or field == 'Date':
                    if self.compare_name(getattr(current_nv,field),getattr(Nv[j],field),field)>=1:
                        Nv[j+1]=Nv[j]
                        j -=1
                    else:
                        break
                elif getattr(current_nv,field)<getattr(Nv[j],field):
                    Nv[j+1]=Nv[j]
                    j -=1
                else:
                    break
                
            Nv[j+1]=current_nv
    def compare_name(self,val1,val2,field):
        cuoi1 = None
        cuoi2 = None

        if field =='Name':
            val1=val1.lower().strip()
            val2=val2.lower().strip()
            
            cuoi1=unidecode(val1.split()[-1])
            cuoi2=unidecode(val2.split()[-1])
        elif field=='Salary':
            cuoi1=self.transpose(val1)
            cuoi2=self.transpose(val2)
        else:
            if field == 'Date':
                # So sánh ngày dưới dạng chuỗi theo định dạng 'dd/mm/yyyy'
                if isinstance(val1, str):
                    val1 = datetime.strptime(val1, "%d/%m/%Y")
                if isinstance(val2, str):
                    val2 = datetime.strptime(val2, "%d/%m/%Y")
                if val1 == val2:
                    return 2
                elif val1 < val2:
                    return 1
                else:
                    return 0
        if cuoi1==cuoi2:
            return 2
        elif cuoi1<cuoi2:
            return 1
        else:
            return 0
    def transpose(self,sal):
        sal=sal.replace("$","")
        try:
            so=float(sal)
            return so   
        except ValueError:
            return None
    def selection_sort(self,field):
        n=self.LenNv()
        Nv=self.nhan_vien
        for i in range(n-1):
            min_index=int(i)
            for j in range(i+1,n):
                if field == 'EmCode' and Nv[j].EmCode < Nv[min_index].EmCode:
                    min_index=j
                elif field == 'Name' and self.compare_name(getattr(Nv[j],field),getattr(Nv[min_index],field),field) >=1:
                    min_index=j
                elif field == 'Date' and self.compare_name(getattr(Nv[j],field),getattr(Nv[min_index],field),field) >=1:
                    min_index=j
                elif field == 'Salary' and self.compare_name(getattr(Nv[j],field),getattr(Nv[min_index],field),field) >=1:
                    min_index=j
                elif field == 'Position' and Nv[j].Position < Nv[min_index].Position:
                    min_index=j
            Nv[i],Nv[min_index]=Nv[min_index],Nv[i]
    def quick_sort(self,arr,field):
        if len(arr) <=1:
            return arr
        
        pivot=arr[len(arr)//2]
        left =[]
        middle = []
        right =[]
        
        for person in arr:
            if field == 'Name' or field == 'Salary' or field == 'Date':
                if self.compare_name(getattr(person,field),getattr(pivot,field),field) == 1:
                    left.append(person)
                elif self.compare_name(getattr(person,field),getattr(pivot,field),field) == 2:
                    middle.append(person)
                else:
                    right.append(person)
            else:
                if getattr(person,field) <getattr(pivot,field):
                    left.append(person)
                elif getattr(person,field)==getattr(pivot,field):
                    middle.append(person)
                else:
                    right.append(person)
        ans = []
        ans =self.quick_sort(left,field)+middle+self.quick_sort(right,field)
        return ans
    def merge_sort(self,Nv,field):
        if len(Nv) <=1:
            return Nv
        
        middle=len(Nv) // 2
        left =Nv[:middle]
        right=Nv[middle:]
        
        # Goi de qui
        left=self.merge_sort(left,field)
        right=self.merge_sort(right,field)
        
        return self.merge(left,right,field)
    def merge(self,left,right,field):
        result=[]
        i=j=0
        
        while i < len(left) and j <len(right):
            if field == 'Name' or field == 'Salary' or field == 'Date':
                if self.compare_name(getattr(left[i],field),getattr(right[j],field),field) >=1:
                    result.append(left[i])
                    i +=1
                else:
                    result.append(right[j])
                    j +=1
            else:
                if getattr(left[i],field) <getattr(right[j],field):
                    result.append(left[i])
                    i +=1
                else:
                    result.append(right[j])
                    j +=1
                    
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    def ShowInfo(self):
        for person in self.nhan_vien:
            print("Employee Code:",person.EmCode)    
            print("Name:",person.Name)
            print("Date:",person.Date)
            print("Position:",person.Position)
            print("Salary:",person.Salary)
            print("\n")
    def to_list(self):
        people_list=[]
        for person in self.nhan_vien:
            person_dict = [
                person.EmCode,
                person.Name,
                person.Date,
                person.Position,
                person.Salary
            ]
            people_list.append(person_dict)
        return people_list

    