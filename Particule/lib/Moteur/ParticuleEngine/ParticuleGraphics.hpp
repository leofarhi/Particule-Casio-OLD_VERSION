#pragma once

#ifndef ClassParticuleGraphics
#define ClassParticuleGraphics
#include "ParticuleBase.hpp"
/*
enum TextureDimension
{
    Unknown,
    None,
    Any,
    Tex2D,
    Tex3D,
    Cube,
    Tex2DArray,
    CubeArray
};

enum FilterMode
{
    Point,
    Bilinear,
    Trilinear
};*/

class Texture : public Object {
    //https://docs.unity3d.com/ScriptReference/Texture.html
public:
    Texture() : Object("None", NULL) {
        textureData = "";
        this->width = 0;
        this->height = 0;
    };
    Texture(const char* name, int width, int height, const unsigned char* Data, const char* UUID=NULL) : Object(name, UUID) {
        textureData = (unsigned char*)Data;
        this->width = width;
        this->height = height;
    };
    unsigned char* textureData;
    /*
    bool allowThreadedTextureCreation;
    int currentTextureMemory;
    int desiredTextureMemory;
    int GenerateAllMips;
    int nonStreamingTextureCount;
    int nonStreamingTextureMemory;
    int streamingMipmapUploadCount;
    int streamingRendererCount;
    int streamingTextureCount;
    bool streamingTextureDiscardUnusedMips;
    bool streamingTextureForceLoadAll;
    int streamingTextureLoadingCount;
    int streamingTexturePendingLoadCount;
    int targetTextureMemory;
    int totalTextureMemory;*/

    //int anisoLevel;
    //TextureDimension dimension;////////
    //FilterMode filterMode;///////////
    //graphicsFormat;//https://docs.unity3d.com/ScriptReference/Experimental.Rendering.GraphicsFormat.html
    int height;
    //imageContentsHash;//https://docs.unity3d.com/ScriptReference/Hash128.html
    //bool isReadable;///////////
    //float mipMapBias;
    //int mipmapCount;
    //int updateCount;
    int width;
    //wrapMode;//https://docs.unity3d.com/ScriptReference/TextureWrapMode.html
    //wrapModeU;
    //wrapModeV;
    //wrapModeW;




};

void ClearScreen();

void UpdateScreen();

void DisplayTexture(Texture* texture, int x, int y, int Zoom, int Rotate);
void DisplayTexture(Texture* texture, int x, int y);

void DrawRectangle(int x, int y, int width, int height, int Color);

void PrintTextMini(unsigned char* text, int x, int y);

#endif