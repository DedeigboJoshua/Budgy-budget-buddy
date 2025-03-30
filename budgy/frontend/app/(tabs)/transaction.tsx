// Add Transaction Screen
// Type: Income or Expense

// Amount

// Category (e.g. groceries, rent, salary)

// Description/Notes (optional)

// Date

// Category type: Necessity or Leisure (for budget suggestions)

import { View, Text, StyleSheet } from 'react-native';
import { Link } from 'expo-router';

export default function Transactions() {
  return (
    <View style={styles.container}>
    <Text style={styles.title}> Transactions </Text>
  </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
    title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
    link: { fontSize: 18, color: 'blue', marginVertical: 10 },
});