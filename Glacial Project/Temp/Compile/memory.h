/****************************************************************/
/*                                                              */
/*                            Memory                            */
/*                                                              */
/*  Description: Fonctions de manipulation de la memoire        */
/*  Auteur:      LePhenixNoir                                   */
/*  Version:     3.0                                            */
/*  Date:        11.06.2014                                     */
/*  Fichier:     memory.h - Fichier d'en-tete                   */
/*                                                              */
/****************************************************************/

#ifndef __MEMORY_H__
  #define __MEMORY_H__


  #define memory_closefile(h)       Bfile_CloseFile(h)
  #define memory_writefile(h,c,l)   Bfile_WriteFile(h,c,l)
  #define memory_readfile(h,b,s,p)  Bfile_ReadFile(h,b,s,p)
  #define memory_seekfile(h,p)      Bfile_SeekFile(h,p)
  #define memory_filesize(h)        Bfile_GetFileSize(h)
  unsigned short *memory_char2font   (char *);

  void memory_seterrors      (int);
  void memory_error          (char *,char *,int);

  int  memory_createfile     (char *,int);
  int  memory_createdir      (char *);
  int  memory_openfile       (char *,int);
  int  memory_deletefile     (char *);

  char **memory_alloc        (int);
  void memory_free           (char **,int);
  int  memory_find           (char *,char **,int);
  int  memory_exists         (char *);
  void *memory_load          (char *);
  int  memory_save           (char *,void *,int);

  int  memory_user_select    (char **,int,int,int);
  void *memory_user_autoload (char *,char *,int,int,int);

#endif
