import requests
import json
def get_data():
    cookies = {
        '__lhash_': 'e807c8ba7d7a9590c3842347b7efdd8a',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '0',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_GUEST_ID': '21864240297',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '1',
        '_gid': 'GA1.2.1612006771.1668704669',
        '_ym_uid': '166870466962144387',
        '_ym_d': '1668704669',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        'partnerSrc': 'yandex',
        'admitad_uid': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        'utm_term': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '297a7a3cf0443ccb15596862ac90a2e9',
        'tmr_lvidTS': '1668704673329',
        'advcake_track_id': '2f614d2e-5a6f-e73f-5c57-e40658c058d2',
        'advcake_session_id': '081175a2-cef7-5884-90f8-aeeef5d252a9',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Perm_Image_Name_Pure_search_desktop%26utm_content%3Dpid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Perm_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3MTs5NTQ3ODExMzUwO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D5695467979067621375',
        'advcake_utm_partner': 'ipr_Perm_Image_Name_Pure_search_desktop',
        'advcake_utm_webmaster': 'pid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop',
        'advcake_click_id': '',
        'uxs_uid': 'e90f0ae0-6699-11ed-aed2-5b483fed63b8',
        'afUserId': '91bbafcc-bc8d-408d-8403-864e1648d7ba-p',
        'AF_SYNC': '1668704674860',
        'flocktory-uuid': 'c53e9756-44e0-4556-8b7b-2917647becd2-7',
        'BIGipServeratg-ps-prod_tcp80': '1678040074.20480.0000',
        'bIPs': '389543560',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1678040074.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_CITY_ID': 'CityCZ_1250',
        'MVID_REGION_ID': '12',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==',
        'cfidsgib-w-mvideo': 'm/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==',
        'cfidsgib-w-mvideo': 'm/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==',
        'gsscgib-w-mvideo': '2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==',
        'gsscgib-w-mvideo': '2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==',
        'fgsscgib-w-mvideo': '1VJVffdecb3d094e698d814943a9cd0b5e9f3e62',
        'fgsscgib-w-mvideo': '1VJVffdecb3d094e698d814943a9cd0b5e9f3e62',
        'cfidsgib-w-mvideo': 'QjR4isOOwnFYqY+synqDLA8kiWHC5bl0vsaKlRRrqOMAH2RkjURDgeLQak5yeR/SVbdQwKQ+esgWgLJEKpOe4H60gj6WwjnWPYQPti7BZ4C22sZ0vmIg0265yVW3fw2HXnziozGgUP927PLqxqpodc7287dYPoQ8EQaSfg==',
        'CACHE_INDICATOR': 'false',
        'MVID_KLADR_ID': '5900000100000',
        'MVID_REGION_SHOP': 'S907',
        'MVID_TIMEZONE_OFFSET': '5',
        'mindboxDeviceUUID': '20c58172-0e70-4289-82e1-55d889d3f1ed',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2220c58172-0e70-4289-82e1-55d889d3f1ed%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'KnbZj2yQ6LR05TVZyby9kKn11dwT7QhjTsnysx9T11fSLlTP1hhZ!1933226215',
        '_sp_id.d61c': '7af553e0-37a4-4ff8-b9de-6eeee7e52054.1668704670.1.1668707029..73f384b4-1eaf-4427-8c1a-50f89bde54d8..67719029-24c0-432a-bde2-535b5fd1823f.1668704669575.104',
        '_ga_CFMZTSS5FM': 'GS1.1.1668704669.1.1.1668707029.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1668704669.1.1.1668707029.60.0.0',
        '_ga': 'GA1.2.1178729003.1668704669',
        'tmr_detect': '1%7C1668707032652',
        'tmr_reqNum': '109',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6c9057d6e29d48efa171503184adae4f,sentry-sample_rate=0%2C5',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=e807c8ba7d7a9590c3842347b7efdd8a; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=0; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21864240297; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=1; _gid=GA1.2.1612006771.1668704669; _ym_uid=166870466962144387; _ym_d=1668704669; _sp_ses.d61c=*; _ym_isad=1; partnerSrc=yandex; admitad_uid=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; utm_term=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=297a7a3cf0443ccb15596862ac90a2e9; tmr_lvidTS=1668704673329; advcake_track_id=2f614d2e-5a6f-e73f-5c57-e40658c058d2; advcake_session_id=081175a2-cef7-5884-90f8-aeeef5d252a9; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Perm_Image_Name_Pure_search_desktop%26utm_content%3Dpid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Perm_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3MTs5NTQ3ODExMzUwO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D5695467979067621375; advcake_utm_partner=ipr_Perm_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop; advcake_click_id=; uxs_uid=e90f0ae0-6699-11ed-aed2-5b483fed63b8; afUserId=91bbafcc-bc8d-408d-8403-864e1648d7ba-p; AF_SYNC=1668704674860; flocktory-uuid=c53e9756-44e0-4556-8b7b-2917647becd2-7; BIGipServeratg-ps-prod_tcp80=1678040074.20480.0000; bIPs=389543560; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1678040074.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; MVID_GEOLOCATION_NEEDED=false; MVID_CITY_ID=CityCZ_1250; MVID_REGION_ID=12; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==; cfidsgib-w-mvideo=m/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==; cfidsgib-w-mvideo=m/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==; gsscgib-w-mvideo=2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==; gsscgib-w-mvideo=2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==; fgsscgib-w-mvideo=1VJVffdecb3d094e698d814943a9cd0b5e9f3e62; fgsscgib-w-mvideo=1VJVffdecb3d094e698d814943a9cd0b5e9f3e62; cfidsgib-w-mvideo=QjR4isOOwnFYqY+synqDLA8kiWHC5bl0vsaKlRRrqOMAH2RkjURDgeLQak5yeR/SVbdQwKQ+esgWgLJEKpOe4H60gj6WwjnWPYQPti7BZ4C22sZ0vmIg0265yVW3fw2HXnziozGgUP927PLqxqpodc7287dYPoQ8EQaSfg==; CACHE_INDICATOR=false; MVID_KLADR_ID=5900000100000; MVID_REGION_SHOP=S907; MVID_TIMEZONE_OFFSET=5; mindboxDeviceUUID=20c58172-0e70-4289-82e1-55d889d3f1ed; directCrm-session=%7B%22deviceGuid%22%3A%2220c58172-0e70-4289-82e1-55d889d3f1ed%22%7D; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; JSESSIONID=KnbZj2yQ6LR05TVZyby9kKn11dwT7QhjTsnysx9T11fSLlTP1hhZ!1933226215; _sp_id.d61c=7af553e0-37a4-4ff8-b9de-6eeee7e52054.1668704670.1.1668707029..73f384b4-1eaf-4427-8c1a-50f89bde54d8..67719029-24c0-432a-bde2-535b5fd1823f.1668704669575.104; _ga_CFMZTSS5FM=GS1.1.1668704669.1.1.1668707029.0.0.0; _ga_BNX5WPP3YK=GS1.1.1668704669.1.1.1668707029.60.0.0; _ga=GA1.2.1178729003.1668704669; tmr_detect=1%7C1668707032652; tmr_reqNum=109; MVID_ENVCLOUD=prod1',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6c9057d6e29d48efa171503184adae4f-a4eb14e8872253d2-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36',
        'x-set-application-id': '280d1e56-e26a-4a6e-8c7e-84cd20ac88bb',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    #print(response)
    products_ids = response.get('body').get('products')
    with open('1_products_ids.json','w') as file:
        json.dump(products_ids,file,indent=4,ensure_ascii=False)

        #print(products_ids)



    cookies = {
        '__lhash_': 'e807c8ba7d7a9590c3842347b7efdd8a',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '0',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_GUEST_ID': '21864240297',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '1',
        '_gid': 'GA1.2.1612006771.1668704669',
        '_ym_uid': '166870466962144387',
        '_ym_d': '1668704669',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        'partnerSrc': 'yandex',
        'admitad_uid': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        'utm_term': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '297a7a3cf0443ccb15596862ac90a2e9',
        'tmr_lvidTS': '1668704673329',
        'advcake_track_id': '2f614d2e-5a6f-e73f-5c57-e40658c058d2',
        'advcake_session_id': '081175a2-cef7-5884-90f8-aeeef5d252a9',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Perm_Image_Name_Pure_search_desktop%26utm_content%3Dpid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Perm_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3MTs5NTQ3ODExMzUwO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D5695467979067621375',
        'advcake_utm_partner': 'ipr_Perm_Image_Name_Pure_search_desktop',
        'advcake_utm_webmaster': 'pid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop',
        'advcake_click_id': '',
        'uxs_uid': 'e90f0ae0-6699-11ed-aed2-5b483fed63b8',
        'afUserId': '91bbafcc-bc8d-408d-8403-864e1648d7ba-p',
        'AF_SYNC': '1668704674860',
        'flocktory-uuid': 'c53e9756-44e0-4556-8b7b-2917647becd2-7',
        'BIGipServeratg-ps-prod_tcp80': '1678040074.20480.0000',
        'bIPs': '389543560',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1678040074.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_CITY_ID': 'CityCZ_1250',
        'MVID_REGION_ID': '12',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==',
        'cfidsgib-w-mvideo': 'm/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==',
        'cfidsgib-w-mvideo': 'm/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==',
        'gsscgib-w-mvideo': '2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==',
        'gsscgib-w-mvideo': '2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==',
        'fgsscgib-w-mvideo': '1VJVffdecb3d094e698d814943a9cd0b5e9f3e62',
        'fgsscgib-w-mvideo': '1VJVffdecb3d094e698d814943a9cd0b5e9f3e62',
        'cfidsgib-w-mvideo': 'QjR4isOOwnFYqY+synqDLA8kiWHC5bl0vsaKlRRrqOMAH2RkjURDgeLQak5yeR/SVbdQwKQ+esgWgLJEKpOe4H60gj6WwjnWPYQPti7BZ4C22sZ0vmIg0265yVW3fw2HXnziozGgUP927PLqxqpodc7287dYPoQ8EQaSfg==',
        'CACHE_INDICATOR': 'false',
        'MVID_KLADR_ID': '5900000100000',
        'MVID_REGION_SHOP': 'S907',
        'MVID_TIMEZONE_OFFSET': '5',
        'mindboxDeviceUUID': '20c58172-0e70-4289-82e1-55d889d3f1ed',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2220c58172-0e70-4289-82e1-55d889d3f1ed%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'KnbZj2yQ6LR05TVZyby9kKn11dwT7QhjTsnysx9T11fSLlTP1hhZ!1933226215',
        '_sp_id.d61c': '7af553e0-37a4-4ff8-b9de-6eeee7e52054.1668704670.1.1668707029..73f384b4-1eaf-4427-8c1a-50f89bde54d8..67719029-24c0-432a-bde2-535b5fd1823f.1668704669575.104',
        '_ga_CFMZTSS5FM': 'GS1.1.1668704669.1.1.1668707029.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1668704669.1.1.1668707029.60.0.0',
        '_ga': 'GA1.2.1178729003.1668704669',
        'tmr_detect': '1%7C1668707032652',
        'tmr_reqNum': '109',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6c9057d6e29d48efa171503184adae4f,sentry-sample_rate=0%2C5',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=e807c8ba7d7a9590c3842347b7efdd8a; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=0; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21864240297; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=1; _gid=GA1.2.1612006771.1668704669; _ym_uid=166870466962144387; _ym_d=1668704669; _sp_ses.d61c=*; _ym_isad=1; partnerSrc=yandex; admitad_uid=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; utm_term=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=297a7a3cf0443ccb15596862ac90a2e9; tmr_lvidTS=1668704673329; advcake_track_id=2f614d2e-5a6f-e73f-5c57-e40658c058d2; advcake_session_id=081175a2-cef7-5884-90f8-aeeef5d252a9; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Perm_Image_Name_Pure_search_desktop%26utm_content%3Dpid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Perm_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3MTs5NTQ3ODExMzUwO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D5695467979067621375; advcake_utm_partner=ipr_Perm_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%257C21914461405_21914461405%257Ccid%257C54501871%257Cgid%257C4285492582%257Caid%257C9547811350%257Cpos%257Cpremium1%257Ckey%257C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%257Caddphrases%257Cno%257Cdvc%257Cdesktop%257Cregion%257C50%257Cregion_name%257C%25D0%259F%25D0%25B5%25D1%2580%25D0%25BC%25D1%258C%257Ccoef_goal%257C0%257Cdesktop; advcake_click_id=; uxs_uid=e90f0ae0-6699-11ed-aed2-5b483fed63b8; afUserId=91bbafcc-bc8d-408d-8403-864e1648d7ba-p; AF_SYNC=1668704674860; flocktory-uuid=c53e9756-44e0-4556-8b7b-2917647becd2-7; BIGipServeratg-ps-prod_tcp80=1678040074.20480.0000; bIPs=389543560; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1678040074.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; MVID_GEOLOCATION_NEEDED=false; MVID_CITY_ID=CityCZ_1250; MVID_REGION_ID=12; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VzfWxjIUkhRmURC0k4MSQdCkAPDh0WQlsoek0MLjp/Xx4yX3INHSVASzs6YGwoSwtDXggzGjxuIGJJWyVFVlJqJh8Xf3IjUw4NYT1HdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFCZSFmT2EmR15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=5MpJlw==; cfidsgib-w-mvideo=m/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==; cfidsgib-w-mvideo=m/Tix46HmEvrP4dHIRVPKcpVd55942DPntZKzQCzSSuiJvOWuQmO95GYTxbx7oRrgdUVJPVoVjGa7Kf9At6PpM0uXKgFs+Eg8CUHy7eZMDb2jwvsym+G96geT663YPuvY49wp0Vj4fsxkhB9GV7odEkmBKV3BDYw+ozhQA==; gsscgib-w-mvideo=2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==; gsscgib-w-mvideo=2SefQlg4J0OI0odNsi3eyA6Uafh+qyJCd7ofYFI4oW84Owq9NjxLK2WQ3Cgp8WBKPl3zPnwe2WQa74/Q7c39mnKWGLh/nYZOTjbNy2HaKw/yy/cK3hTvdUmaGKqjhfOByODzHsPqLNP38hIDQZTerkjoe1+3lPSIwl5L/B48r9kEpDvXBkzIhClcaIZzdZRmSYZ492B/bjla107qUxa8/wGGU5RSZ1eYfNbAHiM7aLPtvLyF9b9zwvDhVsBH2Q==; fgsscgib-w-mvideo=1VJVffdecb3d094e698d814943a9cd0b5e9f3e62; fgsscgib-w-mvideo=1VJVffdecb3d094e698d814943a9cd0b5e9f3e62; cfidsgib-w-mvideo=QjR4isOOwnFYqY+synqDLA8kiWHC5bl0vsaKlRRrqOMAH2RkjURDgeLQak5yeR/SVbdQwKQ+esgWgLJEKpOe4H60gj6WwjnWPYQPti7BZ4C22sZ0vmIg0265yVW3fw2HXnziozGgUP927PLqxqpodc7287dYPoQ8EQaSfg==; CACHE_INDICATOR=false; MVID_KLADR_ID=5900000100000; MVID_REGION_SHOP=S907; MVID_TIMEZONE_OFFSET=5; mindboxDeviceUUID=20c58172-0e70-4289-82e1-55d889d3f1ed; directCrm-session=%7B%22deviceGuid%22%3A%2220c58172-0e70-4289-82e1-55d889d3f1ed%22%7D; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; JSESSIONID=KnbZj2yQ6LR05TVZyby9kKn11dwT7QhjTsnysx9T11fSLlTP1hhZ!1933226215; _sp_id.d61c=7af553e0-37a4-4ff8-b9de-6eeee7e52054.1668704670.1.1668707029..73f384b4-1eaf-4427-8c1a-50f89bde54d8..67719029-24c0-432a-bde2-535b5fd1823f.1668704669575.104; _ga_CFMZTSS5FM=GS1.1.1668704669.1.1.1668707029.0.0.0; _ga_BNX5WPP3YK=GS1.1.1668704669.1.1.1668707029.60.0.0; _ga=GA1.2.1178729003.1668704669; tmr_detect=1%7C1668707032652; tmr_reqNum=109; MVID_ENVCLOUD=prod1',
        'origin': 'https://www.mvideo.ru',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6c9057d6e29d48efa171503184adae4f-bc832bcf8fe9594e-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36',
        'x-set-application-id': '280d1e56-e26a-4a6e-8c7e-84cd20ac88bb',
    }

    json_data = {
        'productIds':products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,json=json_data).json()

    with open('2_items.json','w') as file:
        json.dump(response,file,indent=4,ensure_ascii=False)
        #print(len(response.get('body').get('products')))


        products_ids_str = ','.join(products_ids)

        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,headers=headers).json()

        with open('3_prices.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

        items_prices = {}

        material_prices = response.get('body').get('materialPrices')

        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')

            items_prices[item_id] = {
                'item_basePrice':item_base_price,
                'item_salePrice': item_sale_price,
                'item_bonus':item_bonus
            }

        with open('4_items_prices.json', 'w') as file:
            json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
       products_data=json.load(file)

    with open('4_items_prices.json') as file:
       products_prices=json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if  product_id in products_prices:
            prices =products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
        item['item_link'] = f'https://www.mvideo.ru/products/{item.get("nameTranslit")}-{product_id}'

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()