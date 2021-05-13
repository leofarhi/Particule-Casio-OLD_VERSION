#pragma once
#ifndef ClassParticule
#define ClassParticule
class GameObject;


class SceneManager
{
public:
    SceneManager(int* LstSceneInBuild);
    void LoadScene(int Scene);


    GameObject** AllElem;
    int AllElemLength;
    int CamX;
    int CamY;
private:
    GameObject** SetupAndLoadScene(int Scene);
    int LenOfAllElem(int Scene);
    int ActiveScene;
    int* SceneInBuild;

};
class Component {
public:
    virtual void OnStart() {}
    virtual void OnUpdate() {}

    GameObject* gameObject;
    int classType;
};

class GameObject
{
public:

    GameObject(SceneManager* scene, const unsigned char* init_Img, int init_x, int init_y, int init_w, int init_h, const char* name, const char* type, Component* Compo[], int CompoLength);
    void afficher(int X, int Y);
    //void attaquer(Perso& cible);
    //void morfle(int degat);

//private:

    //int m_vie;
    //int m_attaque;
    //int m_defense;
    unsigned char* Img;
    char* Type;
    char* Name;
    int Static;
    int TrfmImgScale;
    int rotation;
    int x;
    int y;
    int w;
    int h;
    SceneManager* Scene;

    int AllCompoLength;
    Component** AllCompo;
};


#endif