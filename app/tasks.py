from .models import TicketTask
TASKS=[
TicketTask(id='PWD-001',category='password_reset',title='Locked account',description='User cannot sign in after failed passwords.',required_actions=['verify_identity','reset_password','confirm_user'],expected_outcome='Password reset completed.'),
TicketTask(id='VPN-001',category='vpn_fault',title='VPN tunnel failure',description='VPN fails after network change.',required_actions=['collect_network_details','restart_vpn','verify_connection'],expected_outcome='VPN connection restored.'),
TicketTask(id='ACC-001',category='access_request',title='Analytics read access',description='Employee requests read-only analytics access.',required_actions=['verify_manager_approval','grant_read_access','confirm_access'],expected_outcome='Approved read access granted.')]
def get_tasks(): return TASKS
