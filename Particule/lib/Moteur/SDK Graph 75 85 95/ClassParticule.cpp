#include "ClassParticule.h"
#include "MonochromeLib.h"
#include "Images.h"
#include "usefull.h"

GameObject::GameObject(SceneManager* scene, const unsigned char* init_Img, int init_x, int init_y, int init_w, int init_h, const char* name, const char* type, Component* Compo[], int CompoLength)
{
    Img = (unsigned char*)init_Img;
    Name = (char*)name;
    Type = (char*)type;
    Static = 1;
    TrfmImgScale = 100;
    rotation = 90;
    x = init_x;
    y = init_y;
    w = init_w;
    h = init_h;
    AllCompoLength = CompoLength;
    AllCompo = Compo;
    Scene = (SceneManager*)scene;
}
void GameObject::afficher(int X, int Y)
{
    ML_bmp_or_cl((const unsigned char*)Img, x - X, y - Y, w, h);
}
//void Component::OnStart() {}
//void Component::OnUpdate() {}

SceneManager::SceneManager(int* LstSceneInBuild) {
    SceneInBuild = LstSceneInBuild;
    AllElemLength = 0;
    ActiveScene = -1;
    LoadScene(0);
    CamX = 0;
    CamY = 0;

}

void SceneManager::LoadScene(int Scene) {
    if (ActiveScene == Scene) {
        return;
    }
    ActiveScene = Scene;
    for (int i(0); i < AllElemLength; ++i)
    {
        for (int j(0); j < AllElem[i]->AllCompoLength; ++j)
        {
            delete AllElem[i]->AllCompo[j];
        }
        delete AllElem[i];
    }
    AllElem = SetupAndLoadScene(Scene);
    AllElemLength = LenOfAllElem(Scene);
    for (int i(0); i < AllElemLength; ++i) {
        for (int j(0); j < AllElem[i]->AllCompoLength; ++j) {
            GameObject* gameObj = AllElem[i];
            AllElem[i]->AllCompo[j]->gameObject = gameObj;
        }
    }
    for (int i(0); i < AllElemLength; ++i)
    {
        for (int j(0); j < AllElem[i]->AllCompoLength; ++j)
        {
            AllElem[i]->AllCompo[j]->OnStart();
        }
    }
}