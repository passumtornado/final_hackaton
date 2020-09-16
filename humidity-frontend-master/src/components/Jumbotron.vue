<template>
  <div>
    <b-spinner label="Spinning" v-if="!prediction"></b-spinner>
  <b-jumbotron :header="prediction" v-if="prediction" lead="Machine Learning Forecast for Humidity in Sunyani in the next hour">
    <h4>Date: {{ date }}, from {{ hour }}:00 to {{ hour + 1 }}:00</h4>
    <br>
    <b-button variant="primary">
        <router-link to="/manual" style="color: white">Perform Manual Forecast</router-link>
    </b-button>
  </b-jumbotron>
</div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            prediction: '',
            date: new Date().toISOString().slice(0,10),
            hour: new Date().getHours() + 1
        }
    },
    mounted() {
        axios.get('https://api.openweathermap.org/data/2.5/weather?q=Ghana,sunyani&appid=e3311f6761891b3558c08b64e1a9bcf9')
        .then(res => {
            console.log(res.data)
            let temp = res.data.main.temp
            let pressure = res.data.main.pressure
            let wind_speed = res.data.wind.speed
            let hour = new Date().getHours() + 1;
            let day = new Date().getDay();
            let month = new Date().getMonth()

            let data = {
                "temperature": temp,
                "pressure": pressure,
                "wind_speed": wind_speed,
                "hour" :hour,
                "day": day,
                "month": month
            }
            console.log(data);
            
            axios.post('https://humidityforecast.herokuapp.com/api/predict/hourly',
            data).then(response => {
                console.log(response);
                this.prediction = response.data.prediction
                this.prediction = parseFloat(this.prediction.slice(1,-1)).toFixed(3) + '%'
            })
        }).catch(err => {
            console.log(err)
        })
    }
}
</script>

<style>

</style>