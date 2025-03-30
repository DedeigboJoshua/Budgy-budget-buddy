// It’s a set of intro slides or pages that:

// Explain what the app does

// Highlight key features (e.g., "Set goals", "Track spending", "Get insights")

// Make the user feel confident and motivated to use the app

// Example: login.tsx

// to get to this page do http://localhost:8081/onboarding
import { View, Text } from 'react-native';

export default function Onboarding() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Onboarding Screen</Text>
    </View>
  );
}
