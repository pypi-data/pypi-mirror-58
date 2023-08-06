#include "AdsApplovin.h"
#include "ApplovinImpl.h"

AdsApplovin::AdsApplovin()
	: m_appID("")
	, m_bannerAdUnit("")
	, m_interstitialAdUnit("")
	, m_rewardedVideoAdUnit("")
	, m_adsImpl(new ApplovinImpl())
{
	LOG("AdsApplovin()");
}
AdsApplovin::~AdsApplovin()
{
	LOG("~AdsApplovin()");
}

void AdsApplovin::setupApp(const char* adMobAppID, const char* bannerAdUnit, const char* interstitialAdUnit, const char* rewardedVideoAdUnit)
{
	m_appID = adMobAppID;
	m_bannerAdUnit = bannerAdUnit;
	m_interstitialAdUnit = interstitialAdUnit;
	m_rewardedVideoAdUnit = rewardedVideoAdUnit;
}

void AdsApplovin::init()
{
    m_adsImpl->Init();

	m_adsImpl->PlatformInit(m_appID, m_bannerAdUnit, m_interstitialAdUnit, m_rewardedVideoAdUnit);

}

void AdsApplovin::release()
{
	m_adsImpl->PlatformRelease();
}

/*
void AdsApplovin::registerEventListener(AdmobHandlerFunc handler)
{
	//m_HandlerFunc = handler;
	//m_adsImpl->PlatformListener(m_banner_listener, m_rewarded_listener, m_interstitial_listener);
}*/

void AdsApplovin::showBanner(Ads::BannerPosition position, int left, int top)
{
	m_adsImpl->PlatformShowBanner(m_bannerAdUnit, position, left, top);
}

void AdsApplovin::bannerMoveTo(Ads::BannerPosition position, int left, int top)
{
	//m_adsImpl->PlatformBannerMoveTo(position);
	m_adsImpl->PlatformBannerMoveTo(position, left, top);
}

void AdsApplovin::bannerMoveTo(int x, int y)
{
	//m_adsImpl->PlatformBannerMoveTo(x, y);
}

void AdsApplovin::hideBanner()
{
	m_adsImpl->PlatformHideBanner();
}

void AdsApplovin::showInterstitial()
{
	m_adsImpl->PlatformShowInterstitial(m_interstitialAdUnit/*, m_request*/);
}

void AdsApplovin::showRewardedVideo()
{
	m_adsImpl->PlatformShowRewardedVideo(m_rewardedVideoAdUnit/*, m_request*/);
}

void AdsApplovin::pauseRewardedVideo()
{
	//rewarded_video::Pause();
	//WaitForFutureCompletion(rewarded_video::PauseLastResult());
}

void AdsApplovin::resumeRewardedVideo()
{
	//rewarded_video::Resume();
	//WaitForFutureCompletion(rewarded_video::ResumeLastResult());
}