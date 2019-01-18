#include<stdio.h>
#include<stdlib.h>
int main(int argc, char *argv[]){
    int i,a,k,space,space2,i2,a2,k2,space3,space4;
    a=atoi(argv[1]);
    for (i=0;i<a;++i){
        for (k=a-i-2;k>-1;--k){
            printf(" ");

        }
        printf("/");
        for (space=0;space<i;++space){
            printf(" ");
        }
        for (space2=0;space2<i;++space2){
            printf(" ");
        }
        printf("\\");
        for (k=a-i-2;k>-1;--k){
            printf(" ");

        }
        printf("\n");
    }
    for (i2=a-1;i2>-1;--i2){
        for(k2=0;k2<a-i2-1;++k2){
            printf(" ");
        }
        printf("\\");
        for (space3=i2-1;space3>-1;--space3){
            printf(" ");
        }
        for (space4=i2-1;space4>-1;--space4){
            printf(" ");


        }
        printf("/");
        for(k2=0;k2<a-i2-1;++k2){
            printf(" ");
        }
        printf("\n");
    }







return 0;
}
