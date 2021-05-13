/***************************************/
/*            bitmap.c  v0.3           */
/*   créer par Smashmaster 23-12-2012  */
/*      www.planete-casio.fr           */
/***************************************/





#include <BFILE_syscalls.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bitmap.h"


/***********************************************************************************/
/**on déclare ici tous les fonctions que cette lib a besoin pour bien fonctionner **/
/**                        Veillez donc ne pas les supprimer                      **/
/***********************************************************************************/

int PosValeurTab(unsigned short color,unsigned short* sprite8Bit_palette,int end)
{
    int i;
    for (i=0;i<end;i++)
    {
        if (sprite8Bit_palette[i] == color)
            return i;
    }
    return -1;
}


int abso (int x){return (x<0?-x:x);}


unsigned short setColors(unsigned char red, unsigned char green, unsigned char blue)
{
    return (( (31*red/255) & 0x1F) << 11 ) | (( (63*green/255) & 0x3F) << 5 ) | (( (31*blue/255) & 0x1F));
}

void Color16toRgb(int* r, int* g, int* b, short couleur)
{
    *r = (((couleur & 0xf800) >>11)*256)/32;
    *g = (((couleur & 0x7E0) >>5 )*256)/64;
    *b = ((couleur & 0x1F)*256)/32;
}


int strlen (char* str)
{
    int i=0;
    do
    {
        i++;
    }while(str[i] != '\0');
    return i;
}

int InvertHexaNumber (int nombre)
{
    int paquet = 0x000000ff;
    int nombreInvers =0;
    int nbtemp ;
    do
    {
        nbtemp = nombre & paquet;
        nombreInvers <<= 8;
        nombreInvers += nbtemp;
        nombre = nombre/256;
        nombre = nombre & 0x00ffffff;
    }while(nombre !=0);
    return nombreInvers;
}

void plotPx(int x, int y, int color, int alpha) {
   if(x>=0 && x<384 && y>=0 && y<216) {
        unsigned short * base = y * 384 + x +(unsigned short*) 0xA8000000;
        alpha %= 32;
        *base = ((((color & 0xF81F) * alpha + (*base & 0xF81F) * (32-alpha)) >> 5) & 0xF81F) |
            ((((color & 0x07E0) * alpha + (*base & 0x07E0) * (32-alpha)) >> 5) & 0x07E0);
    }
}

int BestColor(unsigned short* palette, unsigned short color)
{
    int min = 256;
    int posMin = 0;
    int i,r1,g1,b1,r2,g2,b2;
    int ecart = 0; 
    for (i=0 ; i<255 ; i++)
    {
        Color16toRgb(&r1,&g1,&b1,color);
        Color16toRgb(&r2,&g2,&b2,palette[i]);
        ecart = ( abso(r1-r2) + abso(g1-g2) + abso(b1-b2) )/3 ;
        if (ecart<min)
        {
            min = ecart;
            posMin = i;
        }
    }
    return posMin;
}


void Read_Header(BITMAP* bmpPicture, int bmpFiles,int bit)
{
    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmFileHeader.type)  , sizeof(short), -1);
    bmpPicture->bmFileHeader.type = InvertHexaNumber (bmpPicture->bmFileHeader.type);
    if (bmpPicture->bmFileHeader.type != BF_MB && bit==16) { bmpPicture->error16bit = ERR_MB; return ; }
    else if (bmpPicture->bmFileHeader.type != BF_MB && bit==8) { bmpPicture->error8bit = ERR_MB; return ; }

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmFileHeader.size_o)  , sizeof(int), -1);
    bmpPicture->bmFileHeader.size_o = InvertHexaNumber (bmpPicture->bmFileHeader.size_o);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmFileHeader.reserved1) , sizeof(short), -1 );
    bmpPicture->bmFileHeader.reserved1 = InvertHexaNumber (bmpPicture->bmFileHeader.reserved1);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmFileHeader.reserved2) , sizeof(short), -1 );
    bmpPicture->bmFileHeader.reserved2 = InvertHexaNumber (bmpPicture->bmFileHeader.reserved2);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmFileHeader.offBits) , sizeof(int), -1 );
    bmpPicture->bmFileHeader.offBits = InvertHexaNumber (bmpPicture->bmFileHeader.offBits);


    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biSize) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biSize = InvertHexaNumber (bmpPicture->bmiHeader.biSize);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->width) , sizeof(int), -1 );
    bmpPicture->width = InvertHexaNumber (bmpPicture->width);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->height) , sizeof(int), -1 );
    bmpPicture->height = InvertHexaNumber (bmpPicture->height);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biPlanes) , sizeof(short), -1 );
    bmpPicture->bmiHeader.biPlanes = InvertHexaNumber (bmpPicture->bmiHeader.biPlanes);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biBitCount) , sizeof(short), -1 );
    bmpPicture->bmiHeader.biBitCount = InvertHexaNumber (bmpPicture->bmiHeader.biBitCount);
    if (bmpPicture->bmiHeader.biBitCount != 24 && bit==16) { bmpPicture->error16bit = ERR_NO24BIT; return ; }
    else if (bmpPicture->bmiHeader.biBitCount != 24 && bit==8) { bmpPicture->error8bit = ERR_NO24BIT; return ; }

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biCompression) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biCompression = InvertHexaNumber (bmpPicture->bmiHeader.biCompression);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biSizeImage) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biSizeImage = InvertHexaNumber (bmpPicture->bmiHeader.biSizeImage);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biXPelsPerMeter) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biXPelsPerMeter = InvertHexaNumber (bmpPicture->bmiHeader.biXPelsPerMeter);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biYPelsPerMeter) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biYPelsPerMeter = InvertHexaNumber (bmpPicture->bmiHeader.biYPelsPerMeter);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biClrUsed) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biClrUsed = InvertHexaNumber (bmpPicture->bmiHeader.biClrUsed);

    Bfile_ReadFile_OS (bmpFiles, &(bmpPicture->bmiHeader.biClrImportant) , sizeof(int), -1 );
    bmpPicture->bmiHeader.biClrImportant = InvertHexaNumber (bmpPicture->bmiHeader.biClrImportant);

}


/***********************************************************************************/
/***********************************************************************************/
/***********************************************************************************/

#ifdef LOADBMP_TO16BITS

void LoadBmp24_to16bits(char *bmp_filename, BITMAP* bmpPicture)
{
    bmpPicture->error16bit = -1;
    int bmpFiles;

    unsigned char r, g, b; //blue

    int i,j,k;

    /**on créér le nom du fichier**/
    unsigned short temp[] = {'\\','\\','f','l','s','0','\\'};
    unsigned short *filename = malloc(sizeof(short)*10+strlen(bmp_filename));
    memcpy(filename,temp,7*sizeof(short));
    for (i=7;i<7+strlen(bmp_filename);i++)
    {
        if (bmp_filename[i-7] == '/')
            filename[i] = '\\';
        else
            filename[i] = bmp_filename[i-7];
    }
    filename[7+strlen(bmp_filename)] = 0;
    /* */


    bmpFiles = Bfile_OpenFile_OS(filename,0);

    if (bmpFiles >= 0)
    {
        Read_Header(bmpPicture, bmpFiles, 16);
        if (bmpPicture->error16bit != ERR_NOERROR)
            return ;

        bmpPicture->sprite16Bit = malloc (sizeof(unsigned short)*bmpPicture->width*bmpPicture->height);
        if (bmpPicture->sprite16Bit == NULL) { bmpPicture->error16bit = ERR_MALLOC; return ; }


        for (i = 0;i<bmpPicture->height;i++)
        {
            for(j=0;j<bmpPicture->width;j++)
            {
                Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &g, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &r, sizeof(char), -1 );
                if (bmpPicture->sprite16Bit != NULL)
                    bmpPicture->sprite16Bit[(bmpPicture->height-i-1)*bmpPicture->width+j] = setColors(r,g,b);
            }
            //patern
            if ((bmpPicture->width*3)%4 != 0)
                for (k=0;k<4-((bmpPicture->width*3)%4);k++)
                    Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
        }
        Bfile_CloseFile_OS(bmpFiles);
    }
    else
    {
        bmpPicture->error16bit = ERR_FILE;
    }
    free (filename);

}

#endif

#ifdef LOADBMP_TO8BITS

void LoadBmp24_to8bits(char *bmp_filename, BITMAP* bmpPicture)
{
    bmpPicture->error8bit = -1;
    int pos=0,nbCouleurDsTableauPalette=0;
    int bmpFiles;

    unsigned char r, g, b; //blue

    int i,j,k;

    /**on créér le nom du fichier**/
    unsigned short temp[] = {'\\','\\','f','l','s','0','\\'};
    unsigned short *filename = malloc(sizeof(short)*10+strlen(bmp_filename));
    memcpy(filename,temp,7*sizeof(short));
    for (i=7;i<7+strlen(bmp_filename);i++) {
        if (bmp_filename[i-7] == '/')
            filename[i] = '\\';
        else
            filename[i] = bmp_filename[i-7];
    }
    filename[7+strlen(bmp_filename)] = 0;
    /**/


    bmpFiles = Bfile_OpenFile_OS(filename,0);
    if (bmpFiles >= 0)
    {
        Read_Header(bmpPicture, bmpFiles,8);
        if (bmpPicture->error8bit != ERR_NOERROR)
            return ;

        bmpPicture->sprite8Bit = malloc (sizeof(unsigned char)*bmpPicture->width*bmpPicture->height);
        if (bmpPicture->sprite8Bit == NULL) { bmpPicture->error8bit = ERR_MALLOC; return ; }


        for (i = 0;i<bmpPicture->height;i++)
        {
            for(j=0;j<bmpPicture->width;j++)
            {
                Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &g, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &r, sizeof(char), -1 );


                if (nbCouleurDsTableauPalette != 0)
                {
                    pos = PosValeurTab(setColors(r,g,b),bmpPicture->sprite8Bit_palette,255);
                    if (pos != -1)
                        bmpPicture->sprite8Bit[(bmpPicture->height-i-1)*bmpPicture->width+j] = pos;
                    else
                    {
                        if ( nbCouleurDsTableauPalette < 256)
                        {
                            bmpPicture->sprite8Bit_palette[nbCouleurDsTableauPalette] = setColors(r,g,b);
                            bmpPicture->sprite8Bit[(bmpPicture->height-i-1)*bmpPicture->width+j] = nbCouleurDsTableauPalette;
                            nbCouleurDsTableauPalette++;
                        }
                        else
                            bmpPicture->sprite8Bit[(bmpPicture->height-i-1)*bmpPicture->width+j] = BestColor(bmpPicture->sprite8Bit_palette, setColors(r,g,b));
                    }
                }
                else
                {
                    bmpPicture->sprite8Bit_palette[nbCouleurDsTableauPalette] = setColors(r,g,b);
                    bmpPicture->sprite8Bit[(bmpPicture->height-i-1)*bmpPicture->width+j] = nbCouleurDsTableauPalette;
                    nbCouleurDsTableauPalette++;
                }

            }
            //patern
            if ((bmpPicture->width*3)%4 != 0)
                for (k=0;k<4-((bmpPicture->width*3)%4);k++)
                    Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
        }

        Bfile_CloseFile_OS(bmpFiles);
    }
    else
    {
        bmpPicture->error8bit = ERR_FILE;
    }
    free (filename);

}

#endif

#ifdef DISPLAY_BMP24

int Display_Bmp24(int x, int y,char* bmp_filename)
{
    BITMAP bmpPicture;
    bmpPicture.error16bit = -1;
    int bmpFiles;

    unsigned char r, g, b; //blue

    int i,j,k;

    /**on créér le nom du fichier**/
    unsigned short temp[] = {'\\','\\','f','l','s','0','\\'};
    unsigned short *filename = malloc(sizeof(short)*10+strlen(bmp_filename));
    memcpy(filename,temp,7*sizeof(short));
    for (i=7;i<7+strlen(bmp_filename);i++)
    {
        if (bmp_filename[i-7] == '/')
            filename[i] = '\\';
        else
            filename[i] = bmp_filename[i-7];
    }
    filename[7+strlen(bmp_filename)] = 0;
    /* */


    bmpFiles = Bfile_OpenFile_OS(filename,0);

    if (bmpFiles >= 0)
    {
        Read_Header(&bmpPicture, bmpFiles,16);
        if (bmpPicture.error16bit != ERR_NOERROR)
            return bmpPicture.error16bit;

        for (i = 0;i<bmpPicture.height;i++)
        {
            for(j=0;j<bmpPicture.width;j++)
            {
                Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &g, sizeof(char), -1 );
                Bfile_ReadFile_OS (bmpFiles, &r, sizeof(char), -1 );
                plotPx( x+j,y+bmpPicture.height-i,setColors(r,g,b),31);
            }
            //patern
            if ((bmpPicture.width*3)%4 != 0)
                for (k=0;k<4-((bmpPicture.width*3)%4);k++)
                    Bfile_ReadFile_OS (bmpFiles, &b, sizeof(char), -1 );
        }
        Bfile_CloseFile_OS(bmpFiles);
    }
    else
    {
        bmpPicture.error16bit = ERR_FILE;
    }
    free(filename);
    return bmpPicture.error16bit;

}

#endif

void Delete_BITMAP(BITMAP* bmpPicture)
{
    if (bmpPicture->error16bit == ERR_NOERROR)
        free(bmpPicture->sprite16Bit);
    if (bmpPicture->error8bit == ERR_NOERROR)
        free(bmpPicture->sprite8Bit);
}

BITMAP Init_BITMAP()
{
    BITMAP bmp;
    int i;

    for (i=0;i<256;i++)
        bmp.sprite8Bit_palette[i] = 0xffff;
    bmp.sprite8Bit = NULL;
    bmp.sprite16Bit = NULL;
    bmp.error8bit = -1;
    bmp.error16bit = -1;

    return bmp;
}
