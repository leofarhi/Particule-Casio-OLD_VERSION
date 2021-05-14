#pragma once
#ifndef ClassParticuleEngine
#define ClassParticuleEngine
#include "Announcement.h"
#include "MonochromeLib.h"
#include "List.h"
#include "usefull.h"
#include "Ressources.h"

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
    List<GameObject*> childs;
public:

    int childCount;
    Vector2 eulerAngles;
    //Vector2 forward;
    bool hasChanged;
    int hierarchyCapacity;
    int hierarchyCount;
    Vector2 localEulerAngles;
    Vector2 localPosition;
    Quaternion* localRotation;
    Vector2 localScale;
    Matrix4x4* localToWorldMatrix;
    Vector2 lossyScale;
    Transform* parent;
    Vector2 position;
    //Vector2 right;
    Transform* root;
    Quaternion* rotation;
    //Vector2 up;
    Matrix4x4* worldToLocalMatrix;

    Transform(GameObject* gameObject, const char* UUID = NULL, const char* name = "Transform") : Component(name,gameObject,UUID){
        childCount = 0;
        eulerAngles = Vector2();
        //forward = None
        hasChanged = NULL;
        hierarchyCapacity = NULL;
        hierarchyCount = NULL;
        localEulerAngles = Vector2();
        localPosition = Vector2();
        localRotation = NULL;
        localScale = Vector2(1,1);
        localToWorldMatrix = NULL;
        lossyScale = Vector2(1,1);
        parent = NULL;
        //childs = []
        position = Vector2();
        //self.right = None
        root = NULL;
        rotation = NULL;
        //self.up = None
        worldToLocalMatrix = NULL;
    };
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
        const unsigned char None[] = { 0x0 };
        textureData = (unsigned char*)None;
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

    void Update() {
        for (int i = 0; i < ListOfComponent.Count; i++)
        {
            ListOfComponent[i]->Update();
        }
    };

    void AddComponent(Component* component) {
        ListOfComponent.Add(component);
    };
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
    void SetActive();
    void TryGetComponent();

    static void CreatePrimitive();
    static void Find();
    static void FindGameObjectsWithTag();
    static void FindWithTag();
};


class Scene {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html
private:
    List<GameObject*> AllGameObject;
public:
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
        float posX = gameObject->transform->position.x;
        float posY = gameObject->transform->position.y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position.x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position.y;
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
        float posX = gameObject->transform->position.x;
        float posY = gameObject->transform->position.y;
        float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position.x;
        float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position.y;
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
    Vector2 velocity;

    Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID = NULL) : MonoBehaviour("Rigidbody", gameObject, UUID) {
        this->Mass = Mass;
        this->UseGravity = UseGravity;
        this->IsKinematic = IsKinematic;
        this->velocity = Vector2();

    };

    void OnStart() {
        this->velocity.Set(0,0);
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
private:
    List<Scene*> AllSceneLoaded;


    Scene* GetSceneInBuild(int index) {
        Scene* newScene = new Scene();

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

//Components


#endif