-- Extension required for the exclusion constraint (equality comparison inside GiST)
CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone_no VARCHAR NOT NULL,
    password_hash VARCHAR NOT NULL
);

CREATE TABLE tables (
    table_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_size INTEGER NOT NULL
);

CREATE TABLE bookings (
    booking_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(user_id),
    table_id UUID NOT NULL REFERENCES tables(table_id),
    time_range TSTZRANGE NOT NULL,
    status VARCHAR NOT NULL DEFAULT 'pending',
    expiry_time TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT now(),
    EXCLUDE USING gist (table_id WITH =, time_range WITH &&)
        WHERE (status <> 'cancelled')
);

CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID NOT NULL UNIQUE REFERENCES bookings(booking_id),
    status VARCHAR NOT NULL DEFAULT 'initiated'
);

CREATE TABLE api_keys (
    key_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    key_value VARCHAR NOT NULL UNIQUE,
    partner_id UUID NOT NULL,
    revoked_at TIMESTAMPTZ,
    requests_per_minute INTEGER NOT NULL DEFAULT 60
);