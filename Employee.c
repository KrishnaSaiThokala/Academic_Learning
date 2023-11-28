
#include<stdio.h>
#include<string.h>
#include<malloc.h>
typedef struct employee
{
    int salary,age,empid;
    char emp_name[50],sex[2];
    struct employee *next;
}s;

s *p,*q,*k,*head,*tail,*t;
void swap()
{
    t->age=p->age;
	p->age=q->age;
	q->age=t->age;
    t->empid=p->empid;
	p->empid=q->empid;
	q->empid=t->empid;
    strcpy(t->emp_name,p->emp_name);
	strcpy(p->emp_name,q->emp_name);
	strcpy(q->emp_name,t->emp_name);
    t->salary=p->salary;
	p->salary=q->salary;
	q->salary=t->salary;
    strcpy(t->sex,p->sex);
	strcpy(p->sex,q->sex);
	strcpy(q->sex,t->sex);

}
void create()
{
    int i;
    p=(s*)malloc(sizeof(s));
    printf("enter employe name:");
    scanf("%s",p->emp_name);
    printf("enter emp id:");
    scanf("%d",&p->empid);
    printf("enter the salary:");
    scanf("%d",&p->salary);
    printf("enter age:");
    scanf("%d",&p->age);
    p->next=NULL;
    if(head==NULL)
        head=p;
    else
        tail->next=p;
    tail=p;
}
void display()
{
for(p=head;p!=NULL;p=p->next)
 {
    printf("employe name  :\t\t%s\n",p->emp_name);
    printf("employe id    :\t\t%d\n",p->empid);
    printf("employe salary:\t\t%d\n",p->salary);
    printf("employee age  :\t\t%d\n",p->age);
}
}
void sort()
{
    int ch;
    printf("\n\n**welcome to sorting**\n\n");
    printf("1.name\n2.emp_id\n3.salary\n4.age\n\n");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1 :    {for(p=head;p!=NULL;p=p->next)
                    {for(q=head;q!=NULL;q=q->next)
                    {if(p->emp_name[0]>q->emp_name[0])
                    {swap();}}
                    }
                    break;}
        case 2 :    {for(p=head;p!=NULL;p=p->next)
                    {for(q=head;q!=NULL;q=q->next)
                    {if(p->empid<q->empid)
                    {swap();}
                    }}break;}
        case 3 :    {for(p=head;p!=NULL;p=p->next)
                    {for(q=head;q!=NULL;q=q->next)
                    {if(p->salary<q->salary)
                    {swap();}}
                    }break;}
        case 4 :    {for(p=head;p!=NULL;p=p->next)
                    {for(q=head;q!=NULL;q=q->next)
                    {if(p->age<q->age)
                    {swap();}
                    }}break;}
    }
}
void search()
{   int id,flag=0;
    printf("enter employee id:");
    scanf("%d",&id);
    for(p=head;p!=NULL;p=p->next)
    {
        if(p->empid==id)
    {
        printf("employe name  :\t\t%s\n",p->emp_name);
        printf("employe id    :\t\t%d\n",p->empid);
        printf("employe salary:\t\t%d\n",p->salary);
        printf("employee age  :\t\t%d\n",p->age);
        flag=1;
    }}
    if(flag==0)
        printf("data not found\n");
}
void delet()
{int id;
    printf("enter employee id number");
    scanf("%d",&id);
    for(p=head;p!=NULL;p=p->next)
      {
          q=p->next;
          if(q->empid==id)
          {
            printf("employe name  :\t\t%s\n",q->emp_name);
            printf("employe id    :\t\t%d\n",q->empid);
            printf("employe salary:\t\t%d\n",q->salary);
            printf("employee age  :\t\t%d\n",q->age);
            printf("*****is dismissed*****\n");
            p->next=q->next;
            free(q);
          }
      }

}
void update()
{
    int id;
    printf("enter employee id number");
    scanf("%d",&id);
    for(p=head;p!=NULL;p=p->next)
       {if(p->empid==id)
         {
            printf("enter name");
            scanf("%s",p->emp_name);
            printf("enter salary");
            scanf("%d",&p->salary);
            printf("enter age:");
            scanf("%d",&p->age);
         }
       }
}
int main()
{
int n,i,ch;
printf("enter no of employees:");
scanf("%d",&n);
for(i=1;i<=n;i++)
create();
do
{
printf("1.insert\n2.delete\n3.search\n4.display\n5.update\n6.sort\n9.exit\n");
scanf("%d",&ch);
switch(ch)
{
case 1:{create();break;}
case 2:{delet();break;}
case 3:{search();break;}
case 4:{display();break;}
case 5:{update();break;}
case 6:{sort();break;}
case 9:{exit(0);break;}
default:printf("select valid option\n");break;
}
}while(ch!=9);
display();
return 0;
}

