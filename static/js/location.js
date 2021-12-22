/* JS for loading city and provinces */
$( document ).ready(function() {
    provinces = {}
    city = {}

    async function getLocationData(url){
        const response = await fetch(url, {
            method: 'GET',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        return response.json();
    }

    var loadProvinceSelect = url => {
        url = url || '/api/get_provinces/';
        getLocationData(url)
        .then(data => {
            if(data.success){
                $('#inputProvince').html('').append(`<option value="0" selected disabled>Select Province</option>`);
                data.provinces.map(province => $('#inputProvince').append(`<option value="${province.name}">${province.name}</option>`));
            }else{
                console.log('Getting provinces returned no result.');
            }
        })
        .catch(e => {
            console.log(e);
            $('#inputProvince').html('');
        });
    }

    var loadCityMuniSelect = (province, baseUrl) => {
        url = baseUrl || '/api/get_citymuni/';
        url = url + province
        getLocationData(url)
        .then(data => {
            if(data.success){
                $('#inputCity').html('').append(`<option value="0" selected disabled>Select City/Muni</option>`);
                data.provinces.map(citymuni => $('#inputCity').append(`<option value="${citymuni.name}">${citymuni.name}</option>`));
            }else{
                console.log('Getting provinces returned no result.');
            }
        })
        .catch(e => {
            console.log(e);
            $('#inputCity').html('');
        });
    }
    

    //Load provinces in the select menu
    loadProvinceSelect();

    //Load City/Muni base on selected province
    $('#inputProvince').on('change', function(){
        province = this.value
        $('#inputCity').html('').append(`<option value="0" selected disabled>Loading...</option>`);
        loadCityMuniSelect(province);
    });
});