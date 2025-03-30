// Settings/Profile Screen
// Change name/email/password

// Reset data

// Toggle dark mode

// Export data (optional)

import { View, Text, StyleSheet } from 'react-native';
import { Link } from 'expo-router';

export default function Profile() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Profile</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  link: { fontSize: 18, color: 'blue' },
});