// Current account balance

// Total income vs expenses (summary)

// Savings goal progress

//Quick add buttons (e.g. "+ Income", "+ Expense")

import { View, Text, StyleSheet } from 'react-native';
import { Link } from 'expo-router';

export default function Dashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dashboard</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  link: { fontSize: 18, color: 'blue', marginVertical: 10 },
});
