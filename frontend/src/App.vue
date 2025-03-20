<template>
  <div class="container">
    <header>
      <h1>Houqin System</h1>
      <p>Campus Flow Management</p>
    </header>
    
    <main>
      <div class="realtime-counter">
        <h2>Current Count</h2>
        <div class="counter-value">{{ currentCount }}</div>
      </div>
      
      <div class="chart-container">
        <h2>Flow History</h2>
        <!-- Chart will be implemented here with VChart -->
        <p>Historical data visualization will appear here</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      currentCount: 0,
      pollingInterval: null,
      apiBaseUrl: 'http://localhost:5000'
    };
  },
  mounted() {
    // Start polling for real-time data
    this.fetchCurrentCount();
    this.pollingInterval = setInterval(() => {
      this.fetchCurrentCount();
    }, 1000); // Poll every second
  },
  beforeUnmount() {
    // Clean up interval when component is destroyed
    if (this.pollingInterval) {
      clearInterval(this.pollingInterval);
    }
  },
  methods: {
    async fetchCurrentCount() {
      try {
        const response = await axios.get(`${this.apiBaseUrl}/api/realtime`);
        this.currentCount = response.data.current_count;
      } catch (error) {
        console.error('Error fetching current count:', error);
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

.realtime-counter {
  text-align: center;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 30px;
}

.counter-value {
  font-size: 72px;
  font-weight: bold;
  color: #333;
}

.chart-container {
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}
</style>
