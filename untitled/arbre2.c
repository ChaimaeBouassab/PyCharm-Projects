#include<stdio.h>
#include<stdlib.h>

typedef struct date{
    int jour;
    int mois;
    int annnee;
}*dat;

typedef struct detailles{
    int destinataire;
    date d;
    float montant;
    struct detailles *suivant;
}det;

typedef struct client{
    struct client *fg;

    int ID;
    char nom[20];
    char prenom[20];
    float solde; 
    det d ;

    struct client *fd; 
}*clt;
//creation dun client

clt creation()
{clt nouveau;
nouveau = (clt)malloc(sizeof(struct client));
printf("id de client :");
scanf("%d",&nouveau->ID);
printf("nom de client :");
scanf("%s",&nouveau->nom);
printf("prenom de client :");
scanf("%s",&nouveau->prenom);

nouveau->fd=NULL;
nouveau->fg=NULL;

return nouveau;

 }

