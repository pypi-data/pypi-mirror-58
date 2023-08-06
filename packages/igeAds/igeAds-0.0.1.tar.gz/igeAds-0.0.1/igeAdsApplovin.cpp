#include "igeAds.h"
#include "igeAds_doc_en.h"

PyObject* adsApplovin_new(PyTypeObject* type, PyObject* args, PyObject* kw)
{
	adsApplovin_obj* self = NULL;

	self = (adsApplovin_obj*)type->tp_alloc(type, 0);
	self->adsApplovin = new AdsApplovin();

	return (PyObject*)self;
}

void adsApplovin_dealloc(adsApplovin_obj* self)
{
	Py_TYPE(self)->tp_free(self);
}

PyObject* adsApplovin_str(adsApplovin_obj* self)
{
	char buf[64];
	snprintf(buf, 64, "ads Applovin object");
	return _PyUnicode_FromASCII(buf, strlen(buf));
}

static PyObject* adsApplovin_Init(adsApplovin_obj* self, PyObject* args, PyObject* kwargs)
{
	//static char* kwlist[] = { "applovinApp","bannerSize", "gender", "childDirectedTreatment","keywords","birthday", "testDevicesIds", NULL };
	static char* kwlist[] = { "android","ios", NULL };
	
	PyObject* applovinAndroid = nullptr;
	PyObject* applovinIos= nullptr;

	if (!PyArg_ParseTupleAndKeywords(args, kwargs, "O|O", kwlist, &applovinAndroid, &applovinIos)) return NULL;

	PyObject* applovinApp = nullptr;
	PyObject* bannerSize = nullptr;
	int gender = 0;
	int childDirectedTreatment;
	PyObject* keywords = nullptr;
	PyObject* birthday = nullptr;
	PyObject* testDevicesIds = nullptr;	

	PyObject* applovinAppPlatform = nullptr;
#if defined(_WIN32) || defined(__ANDROID__)
	if (applovinAndroid && PyTuple_Check(applovinAndroid))
	{
		applovinAppPlatform = applovinAndroid;
	}
#else
	if (applovinIos && PyTuple_Check(applovinIos))
	{
		applovinAppPlatform = applovinIos;
	}
	else
	{
		if (applovinAndroid && PyTuple_Check(applovinAndroid))
		{
			applovinAppPlatform = applovinAndroid;
		}
	}
#endif
	
	if (applovinAppPlatform)
	{
		uint32_t numAttr = 0;
		numAttr = (uint32_t)PyTuple_Size(applovinAppPlatform);

		if (numAttr != 7) {
			PyErr_SetString(PyExc_TypeError, "7 Parameters : applovinApp | bannerSize | gender | childDirectedTreatment | keywords | birthday | testDevicesIds");
			return NULL;
		}

		applovinApp = PyTuple_GET_ITEM(applovinAppPlatform, 0);
		bannerSize = PyTuple_GET_ITEM(applovinAppPlatform, 1);
		gender = PyLong_AsLong(PyTuple_GET_ITEM(applovinAppPlatform, 2));
		childDirectedTreatment = PyLong_AsLong(PyTuple_GET_ITEM(applovinAppPlatform, 3));
		keywords = PyTuple_GET_ITEM(applovinAppPlatform, 4);
		birthday = PyTuple_GET_ITEM(applovinAppPlatform, 5);
		testDevicesIds = PyTuple_GET_ITEM(applovinAppPlatform, 6);
	}
	//if (!PyArg_ParseTupleAndKeywords(args, kwargs, "O|OiiOOO", kwlist, &applovinApp, &bannerSize, &gender, &childDirectedTreatment, &keywords, &birthday, &testDevicesIds)) return NULL;

	if (applovinApp && PyTuple_Check(applovinApp))
	{
        {
            uint32_t numAttr = 0;
            numAttr = (uint32_t) PyTuple_Size(applovinApp);
            if (numAttr != 4) {
                PyErr_SetString(PyExc_TypeError,
                                "4 Parameters : applovinAppID(char*) | bannerAdUnit(char*) | interstitialAdUnit(char*) | rewardedVideoAdUnit(char*)");
                return NULL;
            }
            const char **paramaters = new const char *[numAttr];
            memset(paramaters, 0, sizeof(char *) * numAttr);
            for (uint32_t i = 0; i < numAttr; i++) {
                PyObject *v = PyTuple_GET_ITEM(applovinApp, i);
                paramaters[i] = PyUnicode_AsUTF8(v);
            }
            self->adsApplovin->setupApp(paramaters[0], paramaters[1], paramaters[2],
                                              paramaters[3]);
        }
	}

	self->adsApplovin->init();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject *onAdsApplovinCB = nullptr;

void adsApplovin_ProcessEventCallbackHandler(const char* adsType, int number, const char* reward)
{
	if(onAdsApplovinCB) {

		PyObject *arglist;
		arglist = Py_BuildValue("(sis)", adsType, number, reward);

		PyObject *result = PyEval_CallObject(onAdsApplovinCB, arglist);
		Py_XDECREF(result);
	}
}

PyObject* adsApplovin_RegisterEventListener(adsApplovin_obj* self, PyObject* args)
{
	if (!PyArg_ParseTuple(args, "O", &onAdsApplovinCB))
		return NULL;

	if (!PyCallable_Check(onAdsApplovinCB)) {
		PyErr_SetString(PyExc_TypeError, "Callback function must be a callable object!");
		return NULL;
	}
	Py_XINCREF(onAdsApplovinCB);

	//self->adsApplovin->registerEventListener(adsApplovin_ProcessEventCallbackHandler);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_Release(adsApplovin_obj* self)
{
	self->adsApplovin->release();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_Testcase(adsApplovin_obj* self)
{
	//self->adsAdmob->testcase();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_ShowBanner(adsApplovin_obj* self, PyObject* args)
{
    PyObject* firstParameter = nullptr;
    PyObject* secondParameter = nullptr;
    PyObject* thirdParameter = nullptr;

    if (!PyArg_ParseTuple(args, "|OOO", &firstParameter, &secondParameter, &thirdParameter)) return NULL;
    if (thirdParameter && PyLong_Check(firstParameter) && PyLong_Check(secondParameter) && PyLong_Check(thirdParameter))
    {
        int position = PyLong_AsLong(firstParameter);
        int left = PyLong_AsLong(secondParameter);
        int top = PyLong_AsLong(thirdParameter);
        self->adsApplovin->showBanner((Ads::BannerPosition)position, left, top);
    }
    else if (firstParameter && PyLong_Check(firstParameter))
    {
        int position = PyLong_AsLong(firstParameter);
        self->adsApplovin->showBanner((Ads::BannerPosition)position, 0, 0);
    }
    else
    {
        self->adsApplovin->showBanner((Ads::BannerPosition)0, 0, 0);
    }

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_BannerMoveTo(adsApplovin_obj* self, PyObject* args)
{
	PyObject* firstParameter = nullptr;
    PyObject* secondParameter = nullptr;
    PyObject* thirdParameter = nullptr;

    if (!PyArg_ParseTuple(args, "|OOO", &firstParameter, &secondParameter, &thirdParameter)) return NULL;
    if (thirdParameter && PyLong_Check(firstParameter) && PyLong_Check(secondParameter) && PyLong_Check(thirdParameter))
    {
        int position = PyLong_AsLong(firstParameter);
        int left = PyLong_AsLong(secondParameter);
        int top = PyLong_AsLong(thirdParameter);
        self->adsApplovin->bannerMoveTo((Ads::BannerPosition)position, left, top);
    }
    else if (secondParameter && PyLong_Check(firstParameter) && PyLong_Check(secondParameter))
    {
        int x = PyLong_AsLong(firstParameter);
        int y = PyLong_AsLong(secondParameter);
        self->adsApplovin->bannerMoveTo(x, y);
    }
    else if (firstParameter && PyLong_Check(firstParameter))
    {
        int position = PyLong_AsLong(firstParameter);
        self->adsApplovin->bannerMoveTo((Ads::BannerPosition)position, 0, 0);
    }

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_HideBanner(adsApplovin_obj* self)
{
	self->adsApplovin->hideBanner();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_ShowInterstitial(adsApplovin_obj* self)
{
    self->adsApplovin->showInterstitial();
	
	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_ShowRewardedVideo(adsApplovin_obj* self)
{
	self->adsApplovin->showRewardedVideo();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_PauseRewardedVideo(adsApplovin_obj* self)
{
	self->adsApplovin->pauseRewardedVideo();

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* adsApplovin_ResumeRewardedVideo(adsApplovin_obj* self)
{
	self->adsApplovin->resumeRewardedVideo();

	Py_INCREF(Py_None);
	return Py_None;
}

PyMethodDef adsApplovin_methods[] = {
	{ "init", (PyCFunction)adsApplovin_Init, METH_VARARGS | METH_KEYWORDS, adsAdmobInit_doc },
	{ "release", (PyCFunction)adsApplovin_Release, METH_NOARGS, adsAdmobRelease_doc },
	{ "testcase", (PyCFunction)adsApplovin_Testcase, METH_NOARGS, adsAdmobTestcase_doc },
	{ "showBanner", (PyCFunction)adsApplovin_ShowBanner, METH_VARARGS, adsAdmobShowBanner_doc },
	{ "bannerMoveTo", (PyCFunction)adsApplovin_BannerMoveTo, METH_VARARGS, adsAdmobBannerMoveTo_doc },
	{ "hideBanner", (PyCFunction)adsApplovin_HideBanner, METH_NOARGS, adsAdmobHideBanner_doc },
	{ "showInterstitial", (PyCFunction)adsApplovin_ShowInterstitial, METH_NOARGS, adsAdmobShowInterstitial_doc },
	{ "showRewardedVideo", (PyCFunction)adsApplovin_ShowRewardedVideo, METH_NOARGS, adsAdmobShowRewardedVideo_doc },
	{ "pauseRewardedVideo", (PyCFunction)adsApplovin_PauseRewardedVideo, METH_NOARGS, adsAdmobPauseRewardedVideo_doc },
	{ "resumeRewardedVideo", (PyCFunction)adsApplovin_ResumeRewardedVideo, METH_NOARGS, adsAdmobResumeRewardedVideo_doc },
	{ "registerEventListener", (PyCFunction)adsApplovin_RegisterEventListener, METH_VARARGS, adsAdmobRegisterEventListener_doc },
	{ NULL,	NULL }
};

PyGetSetDef adsApplovin_getsets[] = {
	{ NULL, NULL }
};

PyTypeObject AdsApplovinType = {
	PyVarObject_HEAD_INIT(NULL, 0)
	"igeAds.applovin",							/* tp_name */
	sizeof(adsApplovin_obj),						/* tp_basicsize */
	0,											/* tp_itemsize */
	(destructor)adsApplovin_dealloc,				/* tp_dealloc */
	0,											/* tp_print */
	0,											/* tp_getattr */
	0,											/* tp_setattr */
	0,											/* tp_reserved */
	0,											/* tp_repr */
	0,											/* tp_as_number */
	0,											/* tp_as_sequence */
	0,											/* tp_as_mapping */
	0,											/* tp_hash */
	0,											/* tp_call */
	(reprfunc)adsApplovin_str,						/* tp_str */
	0,											/* tp_getattro */
	0,											/* tp_setattro */
	0,											/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,							/* tp_flags */
	0,											/* tp_doc */
	0,											/* tp_traverse */
	0,											/* tp_clear */
	0,											/* tp_richcompare */
	0,											/* tp_weaklistoffset */
	0,											/* tp_iter */
	0,											/* tp_iternext */
	adsApplovin_methods,							/* tp_methods */
	0,											/* tp_members */
	adsApplovin_getsets,							/* tp_getset */
	0,											/* tp_base */
	0,											/* tp_dict */
	0,											/* tp_descr_get */
	0,											/* tp_descr_set */
	0,											/* tp_dictoffset */
	0,											/* tp_init */
	0,											/* tp_alloc */
	adsApplovin_new,								/* tp_new */
	0,											/* tp_free */
};
