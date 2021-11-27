#pragma once

#ifndef ClassParticuleEngine
#define ClassParticuleEngine
//<LibInclude>
extern "C"
{
#include "keybios.h"
#include "fxlib.h"
#include <stdio.h>
#include "stdio.h"
#include "stdlib.h"

#include "string.h"
#include "time.h"
}

#include "Announcement.h"
#include "ParticuleGraphics.hpp"
#include "List.h"
#include <iostream>
#include <math.h>
#include "usefull.h"
#include "Ressources.h"
#include "ParticuleBase.hpp"
//<\LibInclude>


int Random(int start, int end);

int LenChar(char* txt);

int mod(int x, int m);




enum Tag
{
    Untagged = 0,
    Respawn = 1,
    Finish = 2,
    EditorOnly = 3,
    MainCamera = 4,
    Player = 5,
    GameController = 6
};

enum Layer
{
    Default = 0,
    TransparentFX = 1,
    IgnoreRaycast = 2,
    Water = 3,
    UI = 4
};





class Component : public Object {
    //https://docs.unity3d.com/ScriptReference/Component.html
public:
    //char* tag;
    GameObject* gameObject;
    //Transform* transform;

    Component(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~Component() {};

    /*void BroadcastMessage();
    void CompareTag();
    void GetComponent();
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void TryGetComponent();*/

    ///
    virtual void PhysicsCalculator() {};
    ///

    virtual void Awake() {}
    virtual void FixedUpdate() {}
    virtual void LateUpdate() {}
    /*virtual void OnAnimatorIK() {}
    virtual void OnAnimatorMove() {}
    virtual void OnApplicationFocus() {}
    virtual void OnApplicationPause() {}
    virtual void OnApplicationQuit() {}
    virtual void OnAudioFilterRead() {}
    virtual void OnBecameInvisible() {}
    virtual void OnBecameVisible() {}*/
    //virtual void OnCollisionEnter() {}
    virtual void OnCollisionEnter2D(Collider2D* collider2D) {}/////
    //virtual void OnCollisionExit() {}
    virtual void OnCollisionExit2D(Collider2D* collider2D) {}//////
    //virtual void OnCollisionStay() {}
    virtual void OnCollisionStay2D(Collider2D* collider2D) {}//////
    //virtual void OnConnectedToServer() {}
    virtual void OnControllerColliderHit() {}//////
    virtual void OnDestroy() {}//////
    virtual void OnDisable() {}//////
    /*virtual void OnDisconnectedFromServer() {}
    virtual void OnDrawGizmos() {}
    virtual void OnDrawGizmosSelected() {}*/
    virtual void OnEnable() {}//////
    //virtual void OnFailedToConnect() {}
    //virtual void OnFailedToConnectToMasterServer() {}
    virtual void OnGUI() {}///////
    /*virtual void OnJointBreak() {}
    virtual void OnJointBreak2D() {}
    virtual void OnMasterServerEvent() {}
    virtual void OnMouseDown() {}
    virtual void OnMouseDrag() {}
    virtual void OnMouseEnter() {}
    virtual void OnMouseExit() {}
    virtual void OnMouseOver() {}
    virtual void OnMouseUp() {}
    virtual void OnMouseUpAsButton() {}
    virtual void OnNetworkInstantiate() {}
    virtual void OnParticleCollision() {}
    virtual void OnParticleSystemStopped() {}
    virtual void OnParticleTrigger() {}
    virtual void OnParticleUpdateJobScheduled() {}
    virtual void OnPlayerConnected() {}
    virtual void OnPlayerDisconnected() {}
    virtual void OnPostRender() {}
    virtual void OnPreCull() {}
    virtual void OnPreRender() {}
    virtual void OnRenderImage() {}*/
    virtual void OnRenderObject() {}
    /*virtual void OnSerializeNetworkView() {}
    virtual void OnServerInitialized() {}
    virtual void OnTransformChildrenChanged() {}
    virtual void OnTransformParentChanged() {}*/
    //virtual void OnTriggerEnter() {}
    virtual void OnTriggerEnter2D(Collider2D* collider2D) {}
    //virtual void OnTriggerExit() {}
    virtual void OnTriggerExit2D(Collider2D* collider2D) {}
    //virtual void OnTriggerStay() {}
    virtual void OnTriggerStay2D(Collider2D* collider2D) {}
    virtual void OnValidate() {}//////
    //virtual void OnWillRenderObject() {}
    virtual void Reset() {}/////
    virtual void Start() {}
    virtual void Update() {}
};
class Transform : public Component {
    //https://docs.unity3d.com/ScriptReference/Transform.html
private:
    Vector2* lastPosition;
public:
    List<Transform*> children;
    int childCount;
    //Vector2* eulerAngles;
    //Vector2* forward;
    bool hasChanged;
    int hierarchyCapacity;
    int hierarchyCount;
    //Vector2* localEulerAngles;
    Vector2* localPosition;
    //Quaternion* localRotation;
    //Vector2* localScale;
    //Matrix4x4* localToWorldMatrix;
    Vector2* lossyScale;
    Transform* parent;
    Vector2* position;
    //Vector2* right;
    //Transform* root;
    //Quaternion* rotation;
    //Vector2* up;
    //Matrix4x4* worldToLocalMatrix;

    Transform(GameObject* gameObject, const char* UUID = NULL, const char* name = "Transform");

    ~Transform() {
        delete lastPosition;
        delete localPosition;
        //delete localScale;
        delete position;
    };

    void SetParent(Transform* transform);

    void Start();

    void Update();
};


class Behaviour : public Component {
    //https://docs.unity3d.com/ScriptReference/Behaviour.html
public:

    bool enabled;
    bool isActiveAndEnabled;
    Behaviour(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~Behaviour() {};
};

/*
enum ScaleMode
{
    //https://docs.unity3d.com/ScriptReference/ScaleMode.html
    StretchToFill,
    ScaleAndCrop,
    ScaleToFit,
};
class CallbackEventHandler{
    //https://docs.unity3d.com/ScriptReference/UIElements.CallbackEventHandler.html

};

class Focusable : public CallbackEventHandler {
    //https://docs.unity3d.com/ScriptReference/UIElements.Focusable.html

};

class VisualElement : public Focusable {
    //https://docs.unity3d.com/ScriptReference/UIElements.VisualElement.html

};
*/




class MonoBehaviour : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/MonoBehaviour.html
public:
    //runInEditMode c'est pour l'éditeur donc il n'est pas présent
    bool useGUILayout;

    MonoBehaviour(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~MonoBehaviour() {};

    /*void CancelInvoke();
    void Invoke();
    void InvokeRepeating();
    void IsInvoking();
    void StartCoroutine();
    void StopAllCoroutines();
    void StopCoroutine();*/
    //print c'est pour l'éditeur donc il n'est pas présent
};


class GameObject : public Object {
    //https://docs.unity3d.com/ScriptReference/GameObject.html
public:
    List<Component*> ListOfComponent;
    bool activeInHierarchy;
    bool activeSelf;
    bool isStatic;
    Layer layer;
    Scene* scene;
    long sceneCullingMask;
    Tag tag;
    Transform* transform;

    GameObject(Scene* scene, const char* name, const char* UUID = NULL);

    ~GameObject() {
        for (int i = 0; i < ListOfComponent.Count; i++) {
            delete ListOfComponent.Pop();
        }
        ListOfComponent.Clear();
    };

    bool IsActive();

    void AddComponent(Component* component);
    //void BroadcastMessage();
    //void CompareTag();
    Component* GetComponent(const char* name);
    /*void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void SetActive();
    void TryGetComponent();*/

    //static void CreatePrimitive();
    GameObject* Find(unsigned char* name);
    //static void FindGameObjectsWithTag();
    //static void FindWithTag();
};


class Scene {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html
public:
    List<GameObject*> AllGameObject;
    SceneManager* sceneManager;
    List<Camera*> AllCameras;
    List<Collider2D*> LstColliders;
    //void GetRootGameObjects();
    //bool IsValid();

    ~Scene() {
        for (int i = 0; i < AllGameObject.Count; i++) {
            delete AllGameObject.Pop();
        }
        AllGameObject.Clear();
    }

    void AddGameObject(GameObject* gObj);

    void Update();

    void Start();

    int buildIndex;
    //bool isDirty;
    //bool isLoaded;
    char* name;
    //char* path;
    //int rootCount;

    
};

class Camera : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/Camera.html
public:
    Camera(GameObject* gameObject, const char* UUID = NULL);
};

class Image : public MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:
    //unsigned char* ussClassName;
    Texture* image;
    //scaleMode
    //sourceRect
    //tintColor
    //uv
    //vectorImage

    Image(GameObject* gameObject, Texture* image, const char* UUID = NULL);

    void OnRenderObject();
};

class Sprite : public MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:

    Texture* image;
    bool HaveBackground;


    Sprite(GameObject* gameObject, Texture* image,bool HaveBackground, const char* UUID = NULL);

    void OnRenderObject();
};





class Collider2D : public MonoBehaviour {
    //https://docs.unity3d.com/ScriptReference/Collider2D.html
protected:
    List<Collider2D*> LstColliders;
public:
    bool IsTrigger;
    Collider2D(GameObject* gameObject, bool IsTrigger, const char* UUID = NULL) : MonoBehaviour("Collider2D", gameObject, UUID) {
        gameObject->scene->LstColliders.Add(this);
        this->IsTrigger = IsTrigger;
    };

    void Update();

    bool Contains(Collider2D* collider) {
        for (int o = 0; o < LstColliders.Count; o++) {
            if (collider == LstColliders[o])
                return true;

        }
        return false;
    };

    virtual bool AreTheyTouching(Collider2D* boxCollider) { return false; };
    
};

class BoxCollider2D : public Collider2D {//Collider2D {
    //https://docs.unity3d.com/ScriptReference/BoxCollider2D.html


public:
    Vector2* center;
    Vector2* size;

    BoxCollider2D(GameObject* gameObject,bool IsTrigger,Vector2* center,Vector2* size, const char* UUID = NULL);

    

    bool AreTheyTouching(Collider2D* boxCollider);

    

    ~BoxCollider2D() {
        delete center;
        delete size;
    };
};

class Rigidbody : public MonoBehaviour {
private:
    Collider2D* MyCollider;
    Vector2* lastPosition;

    bool CheckCollider();
    bool IsVisible();
public:
    float Mass;
    bool UseGravity;
    bool IsKinematic;
    Vector2* velocity;

    Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID = NULL);

    void PhysicsCalculator();


    ~Rigidbody() {
        delete velocity;
        delete lastPosition;
    };

    void Start();
    void LateUpdate();

};

class Text : public MonoBehaviour {

public:
    unsigned char* text;

    Text(GameObject* gameObject, unsigned char* text, const char* UUID = NULL);

    void OnRenderObject();


};

class Tilemap : public MonoBehaviour {
public:

    Texture** images;
    int* Datas;
    Vector2* sizeTilemap;
    Vector2* sizeCase;


    Tilemap(GameObject* gameObject, Vector2* sizeTilemap, Vector2* sizeCase, const char* UUID = NULL);

    ~Tilemap() {
        delete[] images;
        delete[] Datas;
    };

    void OnRenderObject();
};


//Components
class ProjectSettings {
public:
    Vector2* Gravity;
    Vector2* ScreenSize;

    
    ProjectSettings() {
        //<ProjectSettings>
        Gravity = new Vector2(/*GravityValue*/);
        ScreenSize = new Vector2(/*ScreenSizeValue*/);
        //<\ProjectSettings>
    };

};
class SceneManager {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html
public:
    int sceneCount;
    static int sceneCountInBuildSettings;
    int LoadSceneAfter;
    bool _quit;
    ProjectSettings* projectSettings;
    
    SceneManager() {
        LoadSceneAfter = -1;
        _quit = false;
        projectSettings = new ProjectSettings();
        LoadTextures();
    }

    //Static Methods
    /*static void CreateScene();
    static void GetActiveScene();
    static void GetSceneAt();
    static void GetSceneByBuildIndex();
    static void GetSceneByName();
    static void GetSceneByPath();*/
    void LoadScene(int index);
    void LoadScene(unsigned char* name);
    /*static void LoadSceneAsync();
    static void MergeScenes();
    static void MoveGameObjectToScene();
    static void SetActiveScene();
    static void UnloadSceneAsync();*/

    GameObject* FindWithName(unsigned char* name);

    //Events
    /*static void activeSceneChanged();
    static void sceneLoaded();
    static void sceneUnloaded();*/

    void UpdateScene();

    void StartScene();

    Texture* Texture_TextureVide;
    //TexturesID

private:
    List<Scene*> AllSceneLoaded;

    void LoadTextures() {
        Texture_TextureVide = new Texture();
        //CreateTextures
    };


    Scene* GetSceneInBuild(int index) {
        Scene* newScene = new Scene();
        newScene->sceneManager = this;

        //AddScenes

        return newScene;

    }

    Scene* GetSceneInBuild(unsigned char* name) {
        unsigned char* AllName[] = { (unsigned char*)"Main" };
        int count = 0;
        for (int i = 0; i < count; i++)
        {
            if (name == AllName[i]) {
                return GetSceneInBuild(i);
            }
        }
        return NULL;
    }
};


void LoadScene(Scene* scene, int nb);

GameObject* FindWithName(unsigned char* name, GameObject* gameObject);

#endif