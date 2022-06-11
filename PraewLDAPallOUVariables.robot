*** Variables ***
${url_login_ldap}    https://iot-apivr.ais.co.th/authtest/v3.2/oauth/authorize?response_type=code&client_id=X6jpUVHVBdszLACYucu%2BmkslzsMyXhwQNG%2Fp1jO1KXg%3D&scope=profile&template_name=index_ldap_cp&redirect_uri=https://www.ais.co.th/
${url_ais}           https://www.ais.th/?code=
${url_get_token}     https://iot-apivr.ais.co.th/authtest/v3.2/oauth/token?client_id=X6jpUVHVBdszLACYucu%2BmkslzsMyXhwQNG%2Fp1jO1KXg%3D&client_secret=clientSecret&grant_type=authorization_code&redirect_uri=https://www.ais.co.th/&code=Ui27w4hUVWgsxH3csON64KbJ98E9i85tyE7K27yUQ5BU
${url_jwt}           https://jwt.io/
