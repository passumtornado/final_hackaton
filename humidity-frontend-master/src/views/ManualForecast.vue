<template>
  <div>

    

  <b-modal ref="my-modal"  title="Machine Learning Humidity Forecast">
    <h3 class="my-4">{{ prediction }}</h3>
  </b-modal>
    <br />
    <Navbar />
    <br />
    <b-form @submit.prevent="predict">
          <b-container class="bv-example-row">
      <b-row>
        <!-- <b-col></b-col> -->
        <b-col sm>
          <label for="example-datepicker">Choose a date</label>
          <b-form-datepicker id="example-datepicker" required v-model="date" class="mb-2"></b-form-datepicker>
          <span style="color:red" v-if="dateError">{{ dateError }}</span>
        </b-col>

        <!-- <b-col></b-col> -->
        <br />
      </b-row>

      <b-row>
        <!-- <b-col></b-col> -->
        <b-col>
          <label for="example-timepicker">Choose the hour</label>
          <b-form-timepicker v-model="time" locale="en" required></b-form-timepicker>
            <span style="color:red" v-if="timeError">{{ timeError }}</span>
        </b-col>

        <!-- <b-col></b-col> -->
      </b-row>

      <br />
      <b-row>
        <!-- <b-col></b-col> -->
        <b-col>
          <label for="example-timepicker">Temperature</label>
          <b-form-input
          type="number"
          step="any"
            v-model="temperature"
            placeholder="Provide the Assumed Temperature"
            required
          ></b-form-input>
        </b-col>

        <!-- <b-col></b-col> -->
      </b-row>
      <br />
      <b-row>
        <!-- <b-col></b-col> -->
        <b-col >
          <label for="example-timepicker">Pressure</label>
          <b-form-input v-model="pressure" type="number" step="any" placeholder="Provide the Assumed Pressure" required></b-form-input>
        </b-col>

        <!-- <b-col></b-col> -->
      </b-row>
<br>
       <b-row>
        <!-- <b-col></b-col> -->
        <b-col>
          <label for="example-timepicker">Windspeed</label>
          <b-form-input v-model="wind_speed" type="number" step="any" placeholder="Provide the Assumed Wind Speed" required></b-form-input>
        </b-col>

        <!-- <b-col></b-col> -->
      </b-row>
    <br>

      <b-row>
        <!-- <b-col></b-col> -->
        <b-col>   
         <b-button variant="primary" type="submit" size="lg">Forecast</b-button>
        </b-col>

        <!-- <b-col></b-col> -->
      </b-row>
    </b-container>
    </b-form>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import axios from 'axios';
export default {
  components: {
    Navbar
  },

  data() {
    return {
      temperature: "",
      pressure: "",
      date: '',
      time: '',
      wind_speed: '',
      prediction: '',
      
      dateError: '',
      timeError: ''
    };
  },

  methods: {
      predict(){
          if (this.date === '') {
              this.dateError = 'The date field is required';
              return;
          } else {
              this.dateError = ''
          }

          if (this.time === '') {
              this.timeError = 'The time field is required'
              return;
          } else {
              this.timeError = ''
          }
          let data = {
              "temperature": this.temperature,
              "pressure": this.pressure,
              "month": new Date(this.date).getMonth(),
              "day": new Date(this.date).getDay(),

              hour: this.time.slice(0,2),
              "wind_speed": this.wind_speed
          }
             axios.post('https://humidityforecast.herokuapp.com/api/predict/hourly',
            data).then(response => {
                console.log(response);
                this.prediction = response.data.prediction
                this.prediction = this.prediction.slice(1,-1) 
                this.showModal();
            })
          console.log(data);
      },

      showModal() {
        this.$refs['my-modal'].show()
      },
  }
};
</script>

<style>
</style>