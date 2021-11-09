#pragma once
#ifndef ClassParticuleEngine
#define ClassParticuleEngine
#include "Announcement.h"
#include "MonochromeLib.h"
#include "List.h"
#include <iostream>
#include <math.h>
#include "usefull.h"
#include "Ressources.h"

int LenChar(char* txt) {
    return strlen(txt);
}

int mod(int x, int m) {
    return (x % m + m) % m;
}

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

class Vector2 {
    //https://docs.unity3d.com/ScriptReference/Vector2.html
public:
    float x;
    float y;
    Vector2() {
        this->x = 0;
        this->y = 0;
    }
    Vector2(float x, float y) {
        this->x = x;
        this->y = y;
    };
    void Set(float x, float y) {
        this->x = x;
        this->y = y;
    };
    void Set(Vector2 vect) {
        this->x = vect.x;
        this->y = vect.y;
    };

    bool operator==(const Vector2& other) {
        return this->x == other.x && this->y == other.y;
    }

    bool operator!=(const Vector2& other) {
        return !(this->x == other.x && this->y == other.y);
    }

    Vector2 operator+(const Vector2& other) {
        return Vector2(this->x + other.x, this->y + other.y);
    }

    Vector2 operator-(const Vector2& other) {
        return Vector2(this->x - other.x, this->y - other.y);
    }

    Vector2 operator*(const Vector2& other) {
        return Vector2(this->x * other.x, this->y * other.y);
    }

    Vector2 operator/(const Vector2& other) {
        return Vector2(this->x / other.x, this->y / other.y);
    }
};

class Quaternion {
    //https://docs.unity3d.com/ScriptReference/Quaternion.html
public:

};

class Matrix4x4 {
    //https://docs.unity3d.com/ScriptReference/Matrix4x4.html
public:

};

class Object {
    //https://docs.unity3d.com/ScriptReference/Object.html
public:
    Object(const char* name, const char* UUID=NULL) {
        this->name = (unsigned char*)name;
        this->ID = (unsigned char*)UUID;
    };

    ~Object() {
        delete name;
        delete ID;
    }
    //hideFlags c'est pour l'éditeur donc il n'est pas présent
    unsigned char* name;

    unsigned char* GetInstanceID() {
        return ID;
    };
    unsigned char* ToString() {
        return name;
    };
    virtual void Destroy() {}
    virtual void DestroyImmediate() {}
    virtual void DontDestroyOnLoad() {}
    virtual void FindObjectOfType() {}
    virtual void FindObjectsOfType() {}
    virtual void Instantiate() {}

    // Overload operator
    bool operator==(const Object& obj) {
        return this->ID == obj.ID;
    }

    bool operator!=(const Object& obj) {
        return this->ID != obj.ID;
    }
private:
    unsigned char* ID;
};

class Component : public Object {
    //https://docs.unity3d.com/ScriptReference/Component.html
public:
    char* tag;
    GameObject* gameObject;
    Transform* transform;

    Component(const char* name, GameObject* gameObject ,const char* UUID = NULL) : Object(name, UUID)
    {
        this->gameObject = gameObject;
    };

    ~Component() {
        delete tag;
    }

    void BroadcastMessage();
    void CompareTag();
    void GetComponent();
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void TryGetComponent();

    virtual void Awake() {}
    virtual void FixedUpdate() {}
    virtual void LateUpdate() {}
    virtual void OnAnimatorIK() {}
    virtual void OnAnimatorMove() {}
    virtual void OnApplicationFocus() {}
    virtual void OnApplicationPause() {}
    virtual void OnApplicationQuit() {}
    virtual void OnAudioFilterRead() {}
    virtual void OnBecameInvisible() {}
    virtual void OnBecameVisible() {}
    virtual void OnCollisionEnter() {}
    virtual void OnCollisionEnter2D() {}
    virtual void OnCollisionExit() {}
    virtual void OnCollisionExit2D() {}
    virtual void OnCollisionStay() {}
    virtual void OnCollisionStay2D() {}
    virtual void OnConnectedToServer() {}
    virtual void OnControllerColliderHit() {}
    virtual void OnDestroy() {}
    virtual void OnDisable() {}
    virtual void OnDisconnectedFromServer() {}
    virtual void OnDrawGizmos() {}
    virtual void OnDrawGizmosSelected() {}
    virtual void OnEnable() {}
    virtual void OnFailedToConnect() {}
    virtual void OnFailedToConnectToMasterServer() {}
    virtual void OnGUI() {}
    virtual void OnJointBreak() {}
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
    virtual void OnRenderImage() {}
    virtual void OnRenderObject() {}
    virtual void OnSerializeNetworkView() {}
    virtual void OnServerInitialized() {}
    virtual void OnTransformChildrenChanged() {}
    virtual void OnTransformParentChanged() {}
    virtual void OnTriggerEnter() {}
    virtual void OnTriggerEnter2D() {}
    virtual void OnTriggerExit() {}
    virtual void OnTriggerExit2D() {}
    virtual void OnTriggerStay() {}
    virtual void OnTriggerStay2D() {}
    virtual void OnValidate() {}
    virtual void OnWillRenderObject() {}
    virtual void Reset() {}
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
    Vector2* localScale;
    //Matrix4x4* localToWorldMatrix;
    Vector2* lossyScale;
    Transform* parent;
    Vector2* position;
    //Vector2* right;
    Transform* root;
    //Quaternion* rotation;
    //Vector2* up;
    //Matrix4x4* worldToLocalMatrix;

    Transform(GameObject* gameObject, const char* UUID = NULL, const char* name = "Transform") : Component(name,gameObject,UUID){
        childCount = 0;
        //eulerAngles = new Vector2();
        //forward = None
        hasChanged = NULL;
        hierarchyCapacity = NULL;
        hierarchyCount = NULL;
        //localEulerAngles = new Vector2();
        localPosition = new Vector2();
        //localRotation = NULL;
        localScale = new Vector2(1,1);
        //localToWorldMatrix = NULL;
        lossyScale = new Vector2(1,1);
        parent = NULL;
        //children = []
        position = new Vector2();
        //self.right = None
        root = NULL;
        //rotation = NULL;
        //self.up = None
        //worldToLocalMatrix = NULL;
        lastPosition = new Vector2();
    };

    ~Transform() {
        //delete localRotation;
        //delete localToWorldMatrix;
        delete parent;
        delete root;
        //delete rotation;
        //delete worldToLocalMatrix;
    }

    void SetParent(Transform* transform) {
        if (parent != NULL) {
            parent->children.Remove(this);
        }
        transform->children.Add(this);
        parent = transform;
    }

    void Start() {
        lastPosition->x = position->x;
        lastPosition->y = position->y;
    }

    void Update() {
        childCount = children.Count;

        if (parent == NULL) {

            if (*position != *localPosition) {
                if (*localPosition != *lastPosition) {
                    position->x = localPosition->x;
                    position->y = localPosition->y;
                }
            }
            localPosition->x = position->x;
            localPosition->y = position->y;
        }
        else
        {
            //return;
            if ((*position != *lastPosition) && (*position == (*localPosition + *parent->position))) {
                localPosition->Set(*localPosition + (*lastPosition - *position));
            }
            position->Set(*localPosition + *parent->position);

        }
        lastPosition->x = position->x;
        lastPosition->y = position->y;
    }
};


class Behaviour : public Component {
    //https://docs.unity3d.com/ScriptReference/Behaviour.html
public:

    bool enabled;
    bool isActiveAndEnabled;
    Behaviour(const char* name, GameObject* gameObject, const char* UUID = NULL) : Component(name,gameObject, UUID) {
        enabled = true;
        isActiveAndEnabled = true;
    };
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
};

class Texture : public Object {
    //https://docs.unity3d.com/ScriptReference/Texture.html
public:
    Texture() : Object("None", NULL) {
        textureData = NULL;
        this->width = 0;
        this->height = 0;
    };
    Texture(const char* name, int width, int height, const unsigned char* Data, const char* UUID = NULL) : Object(name, UUID) {
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
    TextureDimension dimension;
    FilterMode filterMode;
    //graphicsFormat;//https://docs.unity3d.com/ScriptReference/Experimental.Rendering.GraphicsFormat.html
    int height;
    //imageContentsHash;//https://docs.unity3d.com/ScriptReference/Hash128.html
    bool isReadable;
    //float mipMapBias;
    //int mipmapCount;
    //int updateCount;
    int width;
    //wrapMode;//https://docs.unity3d.com/ScriptReference/TextureWrapMode.html
    //wrapModeU;
    //wrapModeV;
    //wrapModeW;

    


};

class MonoBehaviour : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/MonoBehaviour.html
public:
    //runInEditMode c'est pour l'éditeur donc il n'est pas présent
    bool useGUILayout;

    MonoBehaviour(const char* name, GameObject* gameObject, const char* UUID = NULL) : Behaviour(name,gameObject, UUID) {
        useGUILayout = true;
    };

    void CancelInvoke();
    void Invoke();
    void InvokeRepeating();
    void IsInvoking();
    void StartCoroutine();
    void StopAllCoroutines();
    void StopCoroutine();
    //print c'est pour l'éditeur donc il n'est pas présent
};


class GameObject : public Object {
    //https://docs.unity3d.com/ScriptReference/GameObject.html
private:
    List<Component*> ListOfComponent;
public:
    bool activeInHierarchy;
    bool activeSelf;
    bool isStatic;
    Layer layer;
    Scene* scene;
    long sceneCullingMask;
    Tag tag;
    Transform* transform;

    GameObject(Scene* scene,const char* name, const char* UUID = NULL) : Object(name, UUID)
    {
        this->scene = scene;
        this->transform = new Transform(this);
        activeInHierarchy = true;
        activeSelf = true;
        isStatic = false;
        layer = Default;
        sceneCullingMask = NULL;
        tag = Untagged;
        //ListOfComponent.Add(transform);
    };

    ~GameObject() {
        delete transform;
    }

    bool IsActive() {
        if (!activeSelf) {
            activeInHierarchy = false;
            return false;
        }
        if (transform->parent != NULL) {
            if (!transform->parent->gameObject->activeInHierarchy || !transform->parent->gameObject->activeSelf) {
                activeInHierarchy = false;
                return false;
            }
        }
        activeInHierarchy = true;
        return true;
    }

    void Update() {
        this->transform->Update();
        if (!IsActive()) {
            return;
        }
        for (int i = 0; i < ListOfComponent.Count; i++)
        {
            ListOfComponent[i]->Update();
        }
    };

    void Start() {
        this->transform->Start();
        if (!IsActive()) {
            return;
        }
        for (int i = 0; i < ListOfComponent.Count; i++)
        {
            ListOfComponent[i]->Start();
        }
    };

    void AddComponent(Component* component) {
        ListOfComponent.Add(component);
    };
    void BroadcastMessage();
    void CompareTag();
    Component* GetComponent(const char* name) {
        for (int i = 0; i < ListOfComponent.Count; i++)
        {
            if (ListOfComponent[i]->name == (unsigned char*)name)
                return ListOfComponent[i];
        }
        return NULL;
    };
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void SetActive();
    void TryGetComponent();

    static void CreatePrimitive();
    GameObject* Find(unsigned char* name) {
        return FindWithName(name, this);
    };
    static void FindGameObjectsWithTag();
    static void FindWithTag();
};


class Scene {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html
public:
    List<GameObject*> AllGameObject;
    SceneManager* sceneManager;
    void GetRootGameObjects();
    bool IsValid();

    void AddGameObject(GameObject* gObj) {
        AllGameObject.Add(gObj);
    };

    void Update() {
        for (int i = 0; i < AllGameObject.Count; i++)
        {
            AllGameObject[i]->Update();
        }
    };

    void Start() {
        for (int i = 0; i < AllGameObject.Count; i++)
        {
            AllGameObject[i]->Start();
        }
    };

    int buildIndex;
    bool isDirty;
    bool isLoaded;
    char* name;
    //char* path;
    int rootCount;

    List<Camera*> AllCameras;
};

class Camera : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/Camera.html
public:
    Camera(GameObject* gameObject, const char* UUID = NULL) : Behaviour("Camera", gameObject, UUID) {
        gameObject->scene->AllCameras.Add(this);
    }
};

class Image : MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:
    //unsigned char* ussClassName;
    Texture* image;
    //scaleMode
    //sourceRect
    //tintColor
    //uv
    //vectorImage

    Image(GameObject* gameObject, Texture* image, const char* UUID = NULL) : MonoBehaviour("Image", gameObject, UUID) {
        this->image = image;
    };

    void Update() {
        float posX = gameObject->transform->position->x;
        float posY = gameObject->transform->position->y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
        if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
            ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
    };
};

class Sprite : MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:

    Texture* image;


    Sprite(GameObject* gameObject, Texture* image, const char* UUID = NULL) : MonoBehaviour("Sprite", gameObject, UUID) {
        this->image = image;
    };

    void Update() {
        float posX = gameObject->transform->position->x;
        float posY = gameObject->transform->position->y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
        if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
            ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
    };
};


class Rigidbody : MonoBehaviour {
private:
    
public:
    float Mass;
    bool UseGravity;
    bool IsKinematic;
    Vector2* velocity;

    Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID = NULL) : MonoBehaviour("Rigidbody", gameObject, UUID) {
        this->Mass = Mass;
        this->UseGravity = UseGravity;
        this->IsKinematic = IsKinematic;
        this->velocity = new Vector2();

    };

    ~Rigidbody() {
        delete velocity;
    }

    void Start() {
        this->velocity->Set(0,0);
    }
    
};


class Collider2D : MonoBehaviour {
    //https://docs.unity3d.com/ScriptReference/Collider2D.html
public:
    
};

class BoxCollider2D : Collider2D {
    //https://docs.unity3d.com/ScriptReference/BoxCollider2D.html
public:
    
};

class Text : MonoBehaviour {

public:
    unsigned char* text;

    Text(GameObject* gameObject, unsigned char* text, const char* UUID = NULL) : MonoBehaviour("Text", gameObject, UUID) {
        this->text = text;

    };

    void Update() {
        float posX = gameObject->transform->position->x;
        float posY = gameObject->transform->position->y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
        PrintMini((int)(posX - camX), (int)(posY - camY), (unsigned char*)this->text, MINI_OVER);
    }


};

class Tilemap : MonoBehaviour { 
public:

    Texture** images;
    int* Datas;
    Vector2* sizeTilemap;
    Vector2* sizeCase;


    Tilemap(GameObject* gameObject, Vector2* sizeTilemap, Vector2* sizeCase, const char* UUID = NULL) : MonoBehaviour("Tilemap", gameObject, UUID) {
        this->sizeTilemap = sizeTilemap;
        this->sizeCase = sizeCase;
    };

    ~Tilemap() {
        delete[] images;
        delete[] Datas;
    }

    void Start() {

    }

    void Update() {
        float posX = gameObject->transform->position->x;
        float posY = gameObject->transform->position->y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
        for (int h = 0; h < sizeTilemap->y; h++) {
            int x = 0;
            for (int w = h * sizeTilemap->x; w < (h + 1) * sizeTilemap->x; w++) {
                int tempx = (int)((posX - camX) + x * sizeCase->x);
                int tempy = (int)((posY - camY) + h * sizeCase->y);
                if (tempx + sizeCase->x > 0 && tempx < 128 && tempy + sizeCase->y>0 && tempy < 64)
                    ML_bmp_or_cl((const unsigned char*)(images[Datas[w]])->textureData, tempx, tempy, (images[Datas[w]])->width, (images[Datas[w]])->height);
                x++;
            }
        }

    };
};

//Components


class SceneManager {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html
public:
    int sceneCount;
    static int sceneCountInBuildSettings;

    //Static Methods
    static void CreateScene();
    static void GetActiveScene();
    static void GetSceneAt();
    static void GetSceneByBuildIndex();
    static void GetSceneByName();
    static void GetSceneByPath();
    void LoadScene(int index) {
        AllSceneLoaded.Clear();
        AllSceneLoaded.Add(GetSceneInBuild(index));
    };
    void LoadScene(unsigned char* name) {
        AllSceneLoaded.Clear();
        AllSceneLoaded.Add(GetSceneInBuild(name));
    };
    static void LoadSceneAsync();
    static void MergeScenes();
    static void MoveGameObjectToScene();
    static void SetActiveScene();
    static void UnloadSceneAsync();

    GameObject* FindWithName(unsigned char* name) {
        for (int i = 0; i < AllSceneLoaded.Count; i++)
        {
            for (int o = 0; o < AllSceneLoaded[i]->AllGameObject.Count; o++) {
                if (AllSceneLoaded[i]->AllGameObject[o]->name == name) {
                    return AllSceneLoaded[i]->AllGameObject[o];
                }
            }
        }
        return NULL;
    }

    //Events
    static void activeSceneChanged();
    static void sceneLoaded();
    static void sceneUnloaded();

    void UpdateScene() {
        for (int i = 0; i < AllSceneLoaded.Count; i++)
        {
            AllSceneLoaded[i]->Update();
        }
    };

    void StartScene() {
        for (int i = 0; i < AllSceneLoaded.Count; i++)
        {
            AllSceneLoaded[i]->Start();
        }
    }
private:
    List<Scene*> AllSceneLoaded;


    Scene* GetSceneInBuild(int index) {
        Scene* newScene = new Scene();
        newScene->sceneManager = this;

        //AddScenes

        return newScene;

    }

    Scene* GetSceneInBuild(unsigned char* name) {
        unsigned char* AllName[] = {"Main"};
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


void LoadScene(Scene* scene, int nb) {
    scene->sceneManager->LoadScene(nb);
    scene->sceneManager->StartScene();
};

GameObject* FindWithName(unsigned char* name, GameObject* gameObject) {
    return gameObject->scene->sceneManager->FindWithName(name);
};

#endif