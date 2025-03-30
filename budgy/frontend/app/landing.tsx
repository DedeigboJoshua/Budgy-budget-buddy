// 1. Landing Screen / Welcome Page
// App name/logo

// Brief tagline like “Track your spending, grow your savings.”

import { View, Text, StyleSheet } from 'react-native';
import { Link } from 'expo-router';

export default function Landing() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>🏁 Landing Page</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  link: { fontSize: 18, color: 'blue' },
});
