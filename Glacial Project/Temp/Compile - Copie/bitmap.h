/***************************************/
/*            bitmap.h  v0.3           */
/*   créer par Smashmaster 26-12-2012  */
/*      www.planete-casio.fr           */
/***************************************/


#ifndef _BITMAP_H_
#define _BITMAP_H_


/**décommenter les fonction que vous voulez utiliser dans votre programme**/

//#define DISPLAY_BMP24
//#define LOADBMP_TO16BITS
//#define LOADBMP_TO8BITS




/** gestion d'erreur **/
#define ERR_NOERROR -1 //pas d'erreur
#define ERR_FILE 0     //echec lors de l'ouverture du fichier
#define ERR_MB 1       //encodage non supporté, veuillez créer vos fichier bmp sur windows
#define ERR_NO24BIT 2  //Votre fichier bmp n'est pas un fichier 24 bits
#define ERR_MALLOC 3   //Echec lors de l'allocation dynamique de la mémoire, votre image est peut-être trop grande




typedef struct
{
    unsigned short type;
    unsigned int   size_o;
    unsigned short reserved1;
    unsigned short reserved2;
    unsigned int   offBits;
} BITMAPFILEHEADER;

#  define BF_MB 0x4D42

typedef struct
{
    unsigned int   biSize;
    unsigned short biPlanes;
    unsigned short biBitCount;
    unsigned int   biCompression;
    unsigned int   biSizeImage;
    int            biXPelsPerMeter;
    int            biYPelsPerMeter;
    unsigned int   biClrUsed;
    unsigned int   biClrImportant;
} BITMAPINFOHEADER;


typedef struct
{
    BITMAPFILEHEADER bmFileHeader;
    BITMAPINFOHEADER bmiHeader;      /* Image header */
    int width;
    int height;
    unsigned short* sprite16Bit;
    unsigned char* sprite8Bit;
    unsigned short sprite8Bit_palette[256];
	int error16bit;
    int error8bit;

} BITMAP;




#ifdef LOADBMP_TO16BITS
    extern  void LoadBmp24_to16bits(char *bmp_filename, BITMAP* bmpPicture);
#endif
#ifdef LOADBMP_TO8BITS
    extern  void LoadBmp24_to8bits(char *bmp_filename, BITMAP* bmpPicture);
#endif
#ifdef DISPLAY_BMP24
    extern  BITMAP* Display_Bmp24(int x, int y,char *bmp_filename);
#endif

extern  void   Delete_BITMAP(BITMAP* bmp);
extern  BITMAP Init_BITMAP();


#endif

