################################
						# Important #
import time, sys, os, requests
W = "\033[0m"
Y = '\033[33;1m'
LB = '\033[1;36;40m'
################################
def BeforeFlush(Word):
    print (f'{Y}	、__ [~] {LB}{Word} : {W}', end='')
    
def Flush(Which, Color1, Color2, SleepTime1, SleepTime2):
    for char in Which :
        sys.stdout.write(Color1+char+Color2)
        sys.stdout.flush()
        time.sleep(SleepTime1)
    time.sleep(SleepTime2)
    
def ShortLink(Link) :
	ApiUrl = "http://tinyurl.com/api-create.php?url="+Link
	Shorted = requests.get(ApiUrl)
	Flush(Shorted.text, W, W, 0.05, 1)
	
def SaveAsTextFile(SaveThis, FileName) :
	paths = [os.path.join(r,file) for r,d,f in os.walk("Users/") for file in f ]
	if "Users/"+FileName in paths :
		pass
	elif "Users/"+FileName+"/"+FileName+".txt" in paths :
		pass
	else :
		os.system("mkdir Users/"+FileName)
	with open("Users/"+FileName+"/"+FileName+".txt","a+") as File :
		File.write(SaveThis+"\n")
		
		
################################
							# Dump #
################################

def LogginPageId(Data, FileName):
	try :
		BeforeFlush("Loggin Page Id")
		Flush(str(Data["logging_page_id"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Loggin Page Id : "+str(Data["logging_page_id"]), FileName)
	except :
		BeforeFlush("Loggin Page Id")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Loggin Page Id : "+"None", FileName)
	print ("")
		
def ShowSuggestedProfiles(Data, FileName):
	try :
		BeforeFlush("Show Suggested Profiles")
		Flush(str(Data["show_suggested_profiles"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Suggested Profiles : "+str(Data["show_suggested_profiles"]), FileName)
	except :
		BeforeFlush("Show Suggested Profiles")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Suggested Profiles : "+"None", FileName)
	print ("")
		
def ShowFollowDialog(Data, FileName):
	try :
		BeforeFlush("Show Follow Dialog")
		Flush(str(Data["show_follow_dialog"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Follow Dialog : "+str(Data["show_follow_dialog"]), FileName)
	except :
		BeforeFlush("Show Follow Dialog")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show Follow Dialog : "+"None", FileName)
	print ("")

def ShowViewShop(Data, FileName):
	try :
		BeforeFlush("Show View Shop")
		Flush(str(Data["show_view_shop"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Show View Shop : "+str(Data["show_view_shop"]), FileName)
	except :
		BeforeFlush("Show View Shop")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Show View Shop : "+"None", FileName)
	print ("")
	
def Biography(Data, FileName):
	try :
		BeforeFlush("Biography")
		Flush(str(Data["biography"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Biography : "+str(Data["biography"]), FileName)
	except :
		BeforeFlush("Biography")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Biography : "+"None", FileName)
	print ("")

def CountryBlock(Data, FileName):
	try :
		BeforeFlush("Country Block")
		Flush(str(Data["country_block"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Country Block : "+str(Data["country_block"]), FileName)
	except :
		BeforeFlush("Country Block")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Country Block : "+"None", FileName)
	print ("")
	
def ExternalUrl(Data, FileName):
	try :
		BeforeFlush("External Url")
		Flush(str(Data["external_url"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] External Url : "+str(Data["external_url"]), FileName)
	except :
		BeforeFlush("External Url")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] External Url : "+"None", FileName)
	print ("")
	
def ExternalUrlLinkshimmed(Data, FileName):
	try :
		BeforeFlush("External Url Linkshimmed")
		Flush(str(Data["external_url_linkshimmed"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] External Url Linkshimmed : "+str(Data["external_url_linkshimmed"]), FileName)
	except :
		BeforeFlush("External Url Linkshimmed")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] External Url Linkshimmed : "+"None", FileName)
	print ("")
	
def EdgeFollowedBy(Data, FileName):
	try :
		BeforeFlush("Edge Followed By")
		Flush(str(Data["edge_followed_by"]["count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Followed By : "+str(Data["edge_followed_by"]["count"]), FileName)
	except :
		BeforeFlush("Edge Followed By")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Followed By : "+"None", FileName)
	print ("")
	
def Fbid(Data, FileName):
	try :
		BeforeFlush("Fbid")
		Flush(str(Data["fbid"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Fbid : "+str(Data["fbid"]), FileName)
	except :
		BeforeFlush("Fbid")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Fbid : "+"None", FileName)
	print ("")
	
def EdgeFollow(Data, FileName):
	try :
		BeforeFlush("Edge Follow")
		Flush(str(Data["edge_follow"]["count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Follow : "+str(Data["edge_follow"]["count"]), FileName)
	except :
		BeforeFlush("Edge Follow")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Follow : "+"None", FileName)
	print ("")
	
def FullName(Data, FileName):
	try :
		BeforeFlush("Full Name")
		Flush(str(Data["full_name"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Full Name : "+str(Data["full_name"]), FileName)
	except :
		BeforeFlush("Full Name")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Full Name : "+"None", FileName)
	print ("")
	
def HasArEffects(Data, FileName):
	try :
		BeforeFlush("Has Ar Effects")
		Flush(str(Data["has_ar_effects"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Ar Effects : "+str(Data["has_ar_effects"]), FileName)
	except :
		BeforeFlush("Has Ar Effects")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Ar Effects : "+"None", FileName)
	print ("")
	
def HasClips(Data, FileName):
	try :
		BeforeFlush("Has Clips")
		Flush(str(Data["has_clips"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Clips : "+str(Data["has_clips"]), FileName)
	except :
		BeforeFlush("Has Clips")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Clips : "+"None", FileName)
	print ("")
	
def HasGuides(Data, FileName):
	try :
		BeforeFlush("Has Guides")
		Flush(str(Data["has_guides"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Guides : "+str(Data["has_guides"]), FileName)
	except :
		BeforeFlush("Has Guides")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Guides : "+"None", FileName)
	print ("")
	
def HasChannel(Data, FileName):
	try :
		BeforeFlush("Has Channel")
		Flush(str(Data["has_channel"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Channel : "+str(Data["has_channel"]), FileName)
	except :
		BeforeFlush("Has Channel")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Channel : "+"None", FileName)
	print ("")
	
def HighlightReelCount(Data, FileName):
	try :
		BeforeFlush("Highlight Reel Count")
		Flush(str(Data["highlight_reel_count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Highlight Reel Count : "+str(Data["highlight_reel_count"]), FileName)
	except :
		BeforeFlush("Highlight Reel Count")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Highlight Reel Count : "+"None", FileName)
	print ("")
	
def id(Data, FileName):
	try :
		BeforeFlush("id")
		Flush(str(Data["id"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] id : "+str(Data["id"]), FileName)
	except :
		BeforeFlush("id")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] id : "+"None", FileName)
	print ("")
	
def isBusinessAccount(Data, FileName):
	try :
		BeforeFlush("is Business Account")
		Flush(str(Data["is_business_account"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] is Business Account : "+str(Data["is_business_account"]), FileName)
	except :
		BeforeFlush("is Business Account")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] is Business Account : "+"None", FileName)
	print ("")
	
def isJoinedRecently(Data, FileName):
	try :
		BeforeFlush("is Joined Recently")
		Flush(str(Data["is_joined_recently"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] is Joined Recently : "+str(Data["is_joined_recently"]), FileName)
	except :
		BeforeFlush("is Joined Recently")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] is Joined Recently : "+"None", FileName)
	print ("")
	
def BusinessCategoryName(Data, FileName):
	try :
		BeforeFlush("Business Category Name")
		Flush(str(Data["business_category_name"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Business Category Name : "+str(Data["business_category_name"]), FileName)
	except :
		BeforeFlush("Business Category Name")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Business Category Name : "+"None", FileName)
	print ("")
	
def CategoryEnum(Data, FileName):
	try :
		BeforeFlush("Category Enum")
		Flush(str(Data["category_enum"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Category Enum : "+str(Data["category_enum"]), FileName)
	except :
		BeforeFlush("Category Enum")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Category Enum : "+"None", FileName)
	print ("")
	
def isPrivate(Data, FileName):
	try :
		BeforeFlush("is Private")
		Flush(str(Data["is_private"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] is Private : "+str(Data["is_private"]), FileName)
	except :
		BeforeFlush("is Private")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] is Private : "+"None", FileName)
	print ("")
	
def isVerified(Data, FileName):
	try :
		BeforeFlush("is Verified")
		Flush(str(Data["is_verified"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] is Verified : "+str(Data["is_verified"]), FileName)
	except :
		BeforeFlush("is Verified")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] is Verified : "+"None", FileName)
	print ("")
	
def ProfilePicUrlHd(Data, FileName):
	try :
		BeforeFlush("Profile Pic Url Hd")
		ShortLink(str(Data["profile_pic_url_hd"]))
		SaveAsTextFile("[~] Profile Pic Url Hd : "+str(Data["profile_pic_url_hd"]), FileName)
	except :
		BeforeFlush("Profile Pic Url Hd")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Profile Pic Url Hd : "+"None", FileName)
	print ("")
	
def ShouldShowCategory(Data, FileName):
	try :
		BeforeFlush("Should Show Category")
		Flush(str(Data["should_show_category"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Should Show Category : "+str(Data["should_show_category"]), FileName)
	except :
		BeforeFlush("Should Show Category")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Should Show Category : "+"None", FileName)
	print ("")
	
def Username(Data, FileName):
	try :
		BeforeFlush("Username")
		Flush(str(Data["username"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Username : "+str(Data["username"]), FileName)
	except :
		BeforeFlush("Username")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Username : "+"None", FileName)
	print ("")
	
def EdgeFelixVideoTimeline(Data, FileName):
	try :
		BeforeFlush("Edge Felix Video Timeline")
		Flush(str(Data["edge_felix_video_timeline"]["count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Felix Video Timeline : "+str(Data["edge_felix_video_timeline"]["count"]), FileName)
	except :
		BeforeFlush("Edge Felix Video Timeline")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Felix Video Timeline : "+"None", FileName)
	print ("")
	
def EdgeOwnerToTimelineMedia(Data, FileName):
	try :
		BeforeFlush("Edge Owner To Timeline Media")
		Flush(str(Data["edge_owner_to_timeline_media"]["count"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Owner To Timeline Media : "+str(Data["edge_owner_to_timeline_media"]["count"]), FileName)
	except :
		BeforeFlush("Edge Owner To Timeline Media")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Edge Owner To Timeline Media : "+"None", FileName)
	print ("")
	
def OverallCategoryName(Data, FileName):
	try :
		BeforeFlush("Overall Category Name")
		Flush(str(Data["overall_category_name"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Overall Category Name : "+str(Data["overall_category_name"]), FileName)
	except :
		BeforeFlush("Overall Category Name")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Overall Category Name : "+"None", FileName)
	print ("")
	
def CategoryName(Data, FileName):
	try :
		BeforeFlush("Category Name")
		Flush(str(Data["category_name"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Category Name : "+str(Data["category_name"]), FileName)
	except :
		BeforeFlush("Category Name")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Category Name : "+"None", FileName)
	print ("")
	
def ConnectedFbPage(Data, FileName):
	try :
		BeforeFlush("Connected Fb Page")
		Flush(str(Data["connected_fb_page"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Connected Fb Page : "+str(Data["connected_fb_page"]), FileName)
	except :
		BeforeFlush("Connected Fb Page")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Connected Fb Page : "+"None", FileName)
	print ("")
	
def ToastContentOnLoad(Data, FileName):
	try :
		BeforeFlush("Toast Content On Load")
		Flush(str(Data["toast_content_on_load"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Toast Content On Load : "+str(Data["toast_content_on_load"]), FileName)
	except :
		BeforeFlush("Toast Content On Load")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Toast Content On Load : "+"None", FileName)
	print ("")
	
def ProfilePicEditSyncProps(Data, FileName):
	try :
		BeforeFlush("Profile Pic Edit Sync Props")
		Flush(str(Data["profile_pic_edit_sync_props"]), W, W, 0.05, 1)
		SaveAsTextFile("[~] Profile Pic Edit Sync Props : "+str(Data["profile_pic_edit_sync_props"]), FileName)
	except :
		BeforeFlush("Profile Pic Edit Sync Props")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Profile Pic Edit Sync Props : "+"None", FileName)
	print ("")
	
def HasPublicStory(Data, FileName):
	try :
		BeforeFlush("Has Public Story")
		Flush(str(Data), W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Public Story : "+str(Data), FileName)
	except :
		BeforeFlush("Has Public Story")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] Has Public Story : "+"None", FileName)
	print ("")
	
def isLiveNow(Data, FileName):
	try :
		BeforeFlush("is Live Now")
		Flush(str(Data), W, W, 0.05, 1)
		SaveAsTextFile("[~] is Live Now : "+str(Data), FileName)
	except :
		BeforeFlush("is Live Now")
		Flush("None", W, W, 0.05, 1)
		SaveAsTextFile("[~] is Live Now : "+"None", FileName)
	print ("")
