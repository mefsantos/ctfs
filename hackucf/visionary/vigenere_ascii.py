universe = [c for c in (chr(i) for i in range(32,127))]

uni_len = len(universe)

def vign(txt='', key='', typ='d'):
	if not txt:
		print 'Needs text.'
		return
	if not key:
		print 'Needs key.'
		return
	if typ not in ('d', 'e'):
		print 'Type must be "d" or "e".'
		return
	if any(t not in universe for t in key):
		print 'Invalid characters in the key. Must only use ASCII symbols.'
		return

	ret_txt = ''
	k_len = len(key)

	for i, l in enumerate(txt):
		if l not in universe:
			ret_txt += l
		else:
			txt_idx = universe.index(l)

			k = key[i % k_len]
			key_idx = universe.index(k)
			if typ == 'd':
				key_idx *= -1

			code = universe[(txt_idx + key_idx) % uni_len]

			ret_txt += code

	print ret_txt
	return ret_txt

clear = '"So,_did_you_hold_back_during_thattest?"Maybe_a_little,"_Sophronia_admitted._Soapgrinned."That\'s_my_girl."_Sophronia_glared_at_him._He_was_gettingfamiliar."You_are,_miss."_He_continued_togrin."I\'m_my_own_girl,_thank_you_verymuch."―Gail_Carriger'
key = universe
vign(clear, key)