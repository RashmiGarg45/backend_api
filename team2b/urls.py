from django.urls import path
from team2b import views
from team2b import helper_apis

urlpatterns = [
    path("indigo", views.Indigo.as_view(), name="cru_pnr"),
    path("igp", views.IGP.as_view(), name="cru_igp"),
    path("mcdelivery", views.Mcdelivery.as_view(), name="cru_mcdelivery"),
    path("lightinthebox", views.LightInTheBoxAPI.as_view(), name="cru_lightinthebox"),
    path("dominosindo", views.DominosIndo.as_view(), name="cru_dominosindo"),
    path("ostinshop", views.OstinShop.as_view(), name="cru_ostinshop"),
    path("habib", views.HabibOrderIdConstants.as_view(), name="cru_ostinshop"),
    path("watcho", views.WatchoOrderIdsMiningAPI.as_view(), name="cru_watcho"),
    path("watcho/v2", views.WatchoOrderIdsMiningAPIV2.as_view(), name="cru_watcho"),
    path("damnray", views.DamnRayMiningAPI.as_view(), name="cru_damnray"),
    path("pepperfry", views.PepperfryMiningAPI.as_view(), name="cru_damnray"),
    path("mumzworld", views.MumzworldAPI.as_view(), name="cru_mumzworld"),
    path("tripsygames", views.TripsygamesAPI.as_view(), name="cru_tripsygames"),
    path("lazurit", views.LazuritAPI.as_view(), name='cru_lazurit'),
    path("gomcd", views.GomcdAPI.as_view(), name='cru_gomcd'),
    path("bharatmatrimony", views.BharatmatrimonyAPI.as_view(), name='cru_bharatmatrimony'),
    path("samsclub", views.SamsclubAPI.as_view(), name='cru_samsclub'),
    path("weworld", views.WeWorldAPI.as_view(), name='cru_weworld'),
    path("fantoss", views.FantossMiningAPI.as_view(), name='cru_fantoss'),
    path("okeyvip", views.OkeyvipMiningAPI.as_view(), name='cru_okeyvip'),
    path("sephora", views.SephoraMiningAPI.as_view(), name='cru_sephora'),
    path("sephora/v2", views.SephoraMiningAPIV2.as_view(), name='cru_sephora'),
    path("puma", views.PumaMiningAPI.as_view(), name='cru_puma'),
    path("timoclub", views.TimoclubMiningAPI.as_view(), name='cru_timoclub'),
    path("ghnmodd", views.GhnMiningAPI.as_view(), name='cru_ghnmodd'),
    path("rummytime", views.RummytimeMiningAPI.as_view(), name='cru_rummytime'),
    path("scoreone", views.ScoreoneMiningAPI.as_view(), name='cru_scoreone'),
    path("apnatime", views.ApnatimeMiningAPI.as_view(), name='cru_apnatime'),
    path("khiladi", views.KhiladiaddaMiningAPI.as_view(), name='cru_khiladi'),
    path("datingglobal", views.DatingGlobalMiningAPI.as_view(), name='cru_datingglobal'),
    path("datingglobalSubs", views.DatingGlobalSubscribedMiningAPI.as_view(), name='cru_datingglobalSubs'),
    path("indigov2", views.IndigoV2MiningAPI.as_view(), name='cru_indigo'),
    path("indigov2/updatetoken", views.IndigoTokenRefresh.as_view(), name='cru_indigo'),
    path("email", views.EmailIdMiningAPI.as_view(), name='cru_email'),
    path("revenuedata", views.RevenueHelperAPI.as_view(), name='cru_revenuedata'),
    path("phonepestock", views.stock3Api.as_view(), name='phonepestock'),
    path("health", views.ServerHealth.as_view(), name='health'),
    path("fireEvent/player6", views.Player6API.as_view(), name='fireEvent_player6'),
    path("generic_functions", views.GenericScriptFunctions.as_view(), name="generic_functions"),
    path("generic_unusedId_functions", views.GenericUnusedIdScriptFunctions.as_view(), name="generic_unusedId_functions"),
    path("idsimulated", views.SimulatedIdFunction.as_view(), name="idsimulated"),
    path("apps_for_simulation", views.AppsForSimulation.as_view(), name="apps_idsimulated"),
    path("restart_id_service", helper_apis.RestartAPIService.as_view(), name="restart_id_service"),
    path("script_checks", views.ScriptRealtimeChecker.as_view(), name="restart_id_service"),
    path("track_script", views.TrackScript.as_view(), name="track_script"),
    path("script_checks2", views.ScriptRealtimeChecker2.as_view(), name="restart_id_service"),
    path("id/reset", views.ResetOrderId.as_view(), name="restart_id_service"),
    path("bluerewards", views.BluerewardsAPI.as_view(), name="cru_bluerewards"),
    path("holodilink", views.holodilinkAPI.as_view(), name="cru_holodilink"),
    path("rentomojo", views.RentomojoMiningAPI.as_view(), name='cru_rentomojo'),
    path("shahid", views.shahidAPI.as_view(), name="cru_shahid"),
    path("eztravel", views.eztravelAPI.as_view(), name="cru_eztravel"),
    path("betwinner", views.betwinnerAPI.as_view(), name="cru_betwinner"),
    path("tajrummy", views.TajrummyAPI.as_view(), name="cru_tajrummy"),
    path("bet22", views.Bet22API.as_view(), name="cru_bet22"),
    path("ladygentleman", views.ladygentlemanAPI.as_view(), name="cru_ladygentleman"),
    path("igp_idhelper", views.igpAPI.as_view(), name="cru_igp_helper"),
    path("pepperfry_idhelper", views.pepperfryAPI.as_view(), name="cru_pepperfry"),
    path("travelata", views.TravelataAPI.as_view(), name="cru_travelata"),
    path("ontime", views.OntimeAPI.as_view(), name="cru_ontime"),
    path("mcd", views.mcdAPI.as_view(), name="cru_mcd"),
    path("tips_aos_valid", views.tipsAosValidAPI.as_view(), name="cru_tipsAosValidAPI"),
    path("tips_aos_cancelled", views.tipsAosCancelledAPI.as_view(), name="cru_tipsAosCancelledAPI"),
    path("tips_ios_valid", views.tipsIosValidAPI.as_view(), name="cru_tipsIosValidAPI"),
    path("tips_ios_cancelled", views.tipsIosCancelledAPI.as_view(), name="cru_tipsIosCancelledAPI"),
    path("skyline", views.skylineAPI.as_view(), name="cru_skyline"),
    path("reserva", views.ReservaAPI.as_view(), name="cru_reserva"),
    path("gurushort", views.GurushortAPI.as_view(), name="cru_gurushort"),
    path("gurushort_unSubs", views.GurushortNotPremiumAPI.as_view(), name="cru_gurushort_unsubs"),
    path("gurushort_orderid", views.GurushortOrderIdAPI.as_view(), name="cru_gurushort_orderid"),
    path("gurushort_validid", views.GurushortValidAPI.as_view(), name="cru_gurushort_validid"),
    path("credito", views.creditoAPI.as_view(), name="cru_credito"),
    path("ajio", views.AjioAPI.as_view(), name="cru_ajio"),
    path("jungleepoker", views.JungleepokerAPI.as_view(), name="cru_jungleepoker"),
    path("gamerummyprime", views.GameRummyAPI.as_view(), name="cru_gamerummyprime"),
    path("navrang", views.navrangAPI.as_view(), name="cru_navrang"),
    path("lotter38", views.Lotter38API.as_view(), name="cru_lotter38"),
    path("lotter69", views.Lotter69API.as_view(), name="cru_lotter69"),
    path("chaleesultan", views.ChaleeSultanAPI.as_view(), name="cru_chaleesultan"),
    path("ejaby", views.EjabyAPI.as_view(), name="cru_ejaby"),
    path("flappdeals", views.FlappdealsAPI.as_view(), name="cru_flappdeals"),
    path("laundrymate", views.LaundrymateAPI.as_view(), name="cru_laundrymate"),
    path("parimatch", views.ParimatchAPI.as_view(), name="cru_parimatch"),
    path("kisankonnect", views.KisanKonnectAPI.as_view(), name="cru_kisankonnect"),
    path("epocosmetic", views.EpoCosmeticAPI.as_view(), name="cru_epocosmetic"),
    path("ebebek", views.EbebekAPI.as_view(), name="cru_ebebek"),
    path("ebebekuid", views.EbebekuidAPI.as_view(), name="cru_ebebek"),
    path("underarmour", views.UnderarmourAPI.as_view(), name="cru_underarmour"),
    path("underarmourOID", views.UnderarmourOIDAPI.as_view(), name="cru_underarmourOID"),
    path("ping", views.pingAPI.as_view(), name="cru_ping"),
    path("pinoypeso", views.PinoypesoAPI.as_view(), name="cru_pinoypeso"),
    path("ohi", views.OhiAPI.as_view(), name="cru_ohi"),
    path("fivepaisa", views.FivepaisaAPI.as_view(), name="cru_fivepaisa"),
    path("adda", views.AddaAPI.as_view(), name="cru_adda"),
    path("addaOID", views.AddaorderIdAPI.as_view(), name="cru_addaOID"),
    path("bambootauto", views.BambootautoAPI.as_view(), name="cru_bambootauto"),
    path("paynearbyauto", views.PaynearbyAPI.as_view(), name="cru_paynearbyauto"),
    path("in2x", views.in2XAPI.as_view(), name="cru_in2x"),
    path("bluerewardsauto", views.BluerewardsV2API.as_view(), name="cru_bluerewards"),
    path("signnowmodd", views.SignnowAPI.as_view(), name="cru_signnow"),
    path("sixerdream11", views.SixerDreamAPI.as_view(), name="cru_sixer"),
    path("westernunion", views.WesternUnionAPI.as_view(), name="cru_western"),
    path("stolotoUID", views.StolotoUserIdAPI.as_view(), name="cru_stolotoUID"),
    path("stolotoOID", views.StolotoOrderIdAPI.as_view(), name="cru_stolotoOID"),
    path("paysettUID", views.PaysettUserIdAPI.as_view(), name="cru_paysettUID"),
    path("shopeevnUID", views.ShopeevnuidAPI.as_view(), name="cru_shopeevnUID"),
    path("shopeevnOID", views.ShopeevnoidAPI.as_view(), name="cru_shopeevnOID"),
    path("poppolivetmodd", views.PoppoliveAPI.as_view(), name="cru_poppolivetmodd"),
    path("shopeemyUID", views.ShopeemyuidAPI.as_view(), name="cru_shopeemyUID"),
    path("shopeemyOID", views.ShopeemyoidAPI.as_view(), name="cru_shopeemyOID"),
    path("shiprocketcouriert", views.ShiprocketAPI.as_view(), name="cru_shiprocketcouriert"),
    path("novawater", views.NovawaterAPI.as_view(), name="cru_novawater"),
    path("moglix", views.MoglixAPI.as_view(), name="cru_moglix"),
    path("viu", views.ViuAPI.as_view(), name="cru_viu"),
    path("betr", views.BetrAPI.as_view(), name="cru_betr"),
    path("shopeeidUID", views.ShopeeidUIDAPI.as_view(), name="cru_shopeeidUID"),
    path("dupoin", views.DupoinAPI.as_view(), name="cru_dupoin"),
    path("shopeephUID", views.ShopeephUIDAPI.as_view(), name="cru_shopeephUID"),
    path("epikodd", views.EpikoddAPI.as_view(), name="cru_epikodd"),
    path("stoloto", views.StolotoAPI.as_view(), name="cru_stoloto"),
    path("casinopluss", views.CasinoplussAPI.as_view(), name="cru_casinopluss"),
    path("storyland", views.StorylandAPI.as_view(), name="cru_storyland"),
    path("homiedev", views.HomiedevAPI.as_view(), name="cru_homiedev"),
    path("tikett", views.TikettOIDAPI.as_view(), name="cru_tikett"),
    path("apnatimeUID", views.ApnaTimeAPI.as_view(), name="cru_apna"),
    path("motilal", views.MotiLalAPI.as_view(), name="cru_motilal"),
    path("rr_stats", views.ConversionStats.as_view(), name="cru_rr"),
    path("frendipay", views.FrendipayAPI.as_view(), name="cru_frendipay"),
    path("magicland", views.MagiclandAPI.as_view(), name="cru_magicland"),
    path("foxtale", views.FoxtaleMiningAPI.as_view(), name="cru_foxtale"),
    path("hoteltonight", views.HoteltonightAPI.as_view(), name="cru_hoteltonight"),
    path("stoloto_cif", views.stolotoCIFAPI.as_view(), name="cru_stoloto_cif"),
    path("yesmadam", views.YesmadamAPI.as_view(), name="cru_yesmadam"),
    path("beymen", views.BeymenAPI.as_view(), name="cru_beymen"),
    path("bnc", views.BncAPI.as_view(), name="cru_bnc"),
    path("kfc", views.KfcAPI.as_view(), name="cru_kfc"),
    path("jazzcash", views.JazzcashAPI.as_view(), name="cru_jazz"),
    path("petbook", views.PetbookAPI.as_view(), name="cru_petbook"),
    path("tejimaandi", views.tejimaandiAPI.as_view(), name="cru_tejimaandi"),
    path("tejimaandinew", views.TejimaandinewAPI.as_view(), name="cru_tejimaandinew"),
    path("paytmmoneyt", views.PaytmmoneytAPI.as_view(), name="cru_paytmmoneyt"),
    path("anqgoldrewards", views.AnqgoldrewardsAPI.as_view(), name="cru_anqgoldrewards"),
    path("anqgoldrewardscuid", views.AnqgoldrewardscuidAPI.as_view(), name="cru_anqgoldrewardscuid"),
    path("anqgoldrewardsoid", views.AnqgoldrewardsoidAPI.as_view(), name="cru_anqgoldrewardsoid"),
    path("okeyvip2", views.OkeyvipAPI.as_view(), name="cru_okeyvip"),
    path("moneymet", views.MoneymetmodduidAPI.as_view(), name="cru_moneymet"),
    path("imagineart", views.ImagineartAPI.as_view(), name="cru_imagineart"),
    path("parimatchth", views.ParimatchthAPI.as_view(), name="cru_parimatchth"),
    path("melive", views.MeliveAPI.as_view(), name="cru_melivemodd"),
    path("metlive", views.MetliveAPI.as_view(), name="cru_metlivemodd"),
    path("melive_uid", views.MeliveUidAPI.as_view(), name="cru_melivemodd"),
    path("metlive_uid", views.MetliveUidAPI.as_view(), name="cru_metlivemodd"),
    path("opay", views.OpayAPI.as_view(), name="cru_opay"),
    path("bevietnames", views.BevietnamesAPI.as_view(), name="cru_bevietnames"),
]